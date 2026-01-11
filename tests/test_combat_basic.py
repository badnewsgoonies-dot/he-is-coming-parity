from he_is_coming.engine.combat import CombatResolver, CombatState, Combatant
from he_is_coming.engine.rng import RNG
from he_is_coming.systems.inventory import Inventory


def test_basic_combat_player_wins():
    resolver = CombatResolver()
    player = Combatant(actor_id="player", max_hp=10, hp=10, attack=4, armor=0, speed=3, inventory=Inventory(4))
    enemy = Combatant(actor_id="enemy", max_hp=8, hp=8, attack=2, armor=0, speed=2, inventory=Inventory(4))
    state = CombatState(player=player, enemy=enemy)
    resolver.resolve(state, RNG(1))
    assert state.player.alive
    assert not state.enemy.alive
