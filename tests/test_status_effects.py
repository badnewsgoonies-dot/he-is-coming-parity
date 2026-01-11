from he_is_coming.engine.combat import CombatResolver, CombatState, Combatant
from he_is_coming.engine.rng import RNG
from he_is_coming.engine.status import Status
from he_is_coming.systems.inventory import Inventory


def test_thorns_damage_reflects():
    resolver = CombatResolver()
    player = Combatant(actor_id="player", max_hp=10, hp=10, attack=3, armor=0, speed=3, inventory=Inventory(4))
    enemy = Combatant(actor_id="enemy", max_hp=10, hp=10, attack=1, armor=0, speed=2, inventory=Inventory(4))
    enemy.statuses.add(Status.THORNS, 2)
    state = CombatState(player=player, enemy=enemy)
    resolver.resolve(state, RNG(1), max_turns=1)
    assert state.player.hp == 8


def test_stun_skips_attack():
    resolver = CombatResolver()
    player = Combatant(actor_id="player", max_hp=10, hp=10, attack=5, armor=0, speed=3, inventory=Inventory(4))
    enemy = Combatant(actor_id="enemy", max_hp=10, hp=10, attack=1, armor=0, speed=2, inventory=Inventory(4))
    player.statuses.add(Status.STUN, 1)
    state = CombatState(player=player, enemy=enemy)
    resolver.resolve(state, RNG(1), max_turns=1)
    assert state.enemy.hp == 10
