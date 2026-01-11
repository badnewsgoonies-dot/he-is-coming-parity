from dataclasses import dataclass, field

from he_is_coming.engine.status import Status, StatusState
from he_is_coming.engine.triggers import Trigger, TriggerEffect, TriggerEvent
from he_is_coming.systems.inventory import Inventory


@dataclass
class Combatant:
    actor_id: str
    max_hp: int
    hp: int
    attack: int
    armor: int
    speed: int
    inventory: Inventory
    statuses: StatusState = field(default_factory=StatusState)
    triggered_wounded: bool = False
    triggered_exposed: bool = False

    @property
    def alive(self) -> bool:
        return self.hp > 0


@dataclass
class CombatState:
    player: Combatant
    enemy: Combatant
    events: list[TriggerEvent] = field(default_factory=list)


class CombatResolver:
    """Resolves auto-battle outcomes using ordered triggers."""

    def resolve(self, state: CombatState, rng, max_turns: int = 100) -> CombatState:
        self._emit_trigger(state, state.player, state.enemy, Trigger.BATTLE_START)
        self._emit_trigger(state, state.enemy, state.player, Trigger.BATTLE_START)

        for _ in range(max_turns):
            if not state.player.alive or not state.enemy.alive:
                break
            turn_order = self._turn_order(state.player, state.enemy)
            for actor, target in turn_order:
                if not actor.alive or not target.alive:
                    break
                if self._apply_stun(actor):
                    continue
                damage = self._compute_damage(actor, target)
                self._apply_damage(target, damage)
                self._apply_thorns(actor, target)
                self._emit_trigger(state, actor, target, Trigger.ON_HIT)
                self._check_threshold_triggers(state, actor, target)
                self._apply_end_turn(actor)
                if not target.alive:
                    break

        return state

    def _turn_order(self, player: Combatant, enemy: Combatant):
        if player.speed >= enemy.speed:
            return [(player, enemy), (enemy, player)]
        return [(enemy, player), (player, enemy)]

    def _compute_damage(self, actor: Combatant, target: Combatant) -> int:
        attack = actor.attack
        if actor.statuses.has(Status.FREEZE):
            attack = max(1, attack // 2)
        return max(0, attack)

    def _apply_damage(self, target: Combatant, damage: int) -> None:
        if damage <= 0:
            return
        if target.armor >= damage:
            target.armor -= damage
        else:
            remaining = damage - target.armor
            target.armor = 0
            target.hp = max(0, target.hp - remaining)

    def _apply_thorns(self, actor: Combatant, target: Combatant) -> None:
        thorns = target.statuses.get(Status.THORNS)
        if thorns > 0 and actor.alive:
            actor.hp = max(0, actor.hp - thorns)
            target.statuses.remove(Status.THORNS, thorns)

    def _apply_stun(self, actor: Combatant) -> bool:
        if actor.statuses.has(Status.STUN):
            actor.statuses.remove(Status.STUN, 1)
            return True
        return False

    def _apply_end_turn(self, actor: Combatant) -> None:
        if actor.statuses.has(Status.POISON):
            dmg = actor.statuses.get(Status.POISON)
            actor.hp = max(0, actor.hp - dmg)
            actor.statuses.remove(Status.POISON, 1)
        if actor.statuses.has(Status.RIPTIDE):
            dmg = actor.statuses.get(Status.RIPTIDE)
            actor.hp = max(0, actor.hp - dmg)
            actor.statuses.remove(Status.RIPTIDE, 1)
        if actor.statuses.has(Status.ACID) and actor.armor > 0:
            reduction = min(actor.armor, actor.statuses.get(Status.ACID))
            actor.armor -= reduction
            actor.statuses.remove(Status.ACID, 1)
        if actor.statuses.has(Status.FREEZE):
            actor.statuses.remove(Status.FREEZE, 1)

    def _check_threshold_triggers(self, state: CombatState, actor: Combatant, target: Combatant) -> None:
        for unit in (actor, target):
            if not unit.triggered_wounded and unit.hp <= max(1, unit.max_hp // 2):
                unit.triggered_wounded = True
                self._emit_trigger(state, unit, None, Trigger.WOUNDED)
            if not unit.triggered_exposed and unit.armor == 0:
                unit.triggered_exposed = True
                self._emit_trigger(state, unit, None, Trigger.EXPOSED)

    def _emit_trigger(self, state: CombatState, actor: Combatant, target: Combatant | None, trigger: Trigger) -> None:
        source = f"{actor.actor_id}:{trigger.value}"
        state.events.append(TriggerEvent(trigger=trigger, actor_id=actor.actor_id, target_id=target.actor_id if target else None, source=source))
        for effect in actor.inventory.iter_trigger_effects(trigger):
            self._apply_effect(actor, target, effect)

    def _apply_effect(self, actor: Combatant, target: Combatant | None, effect: TriggerEffect) -> None:
        destination = actor if effect.effect.target == "self" else target
        if destination is None:
            return
        kind = effect.effect.kind
        amount = effect.effect.amount or 0
        if kind == "damage":
            self._apply_damage(destination, amount)
        elif kind == "heal":
            destination.hp = min(destination.max_hp, destination.hp + amount)
        elif kind == "armor":
            destination.armor += amount
        elif kind == "status" and effect.effect.status is not None:
            destination.statuses.add(effect.effect.status, amount or 1)
