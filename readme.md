# Fentanyl Quest Redux

Fork of the original Fentanyl Quest.
A simple turn-based dungeon explorer, played on your terminal.

## TODO
- [ ] Finish kakapoop path
- [ ] Save progress to disk
- [ ] More story

## Maybe TODO (ideas)
- [ ] Different classes for each attack?

## changelog

### v1.2 (Alpha)
- `coolTransition()` default value changed
- `calculateAttack()` switched out for `handleAttack()`, which handles both the player and enemy
- added prototype stats display for player and enemy during battle
- added a lot of delays
- added very basic debug mode
- player attack damage is no longer based off of the enemy's strength (wtf)
- unmemed the licence

### v1.1 (Alpha)
- `delayPrint()` a function to both print and delay for a variable amount of time
- `coolTransition()` added an optional amount of time to sleep to the after the transition
- removed 2 useless brackets for maximum efficiency
- enemy can not attack the player when it is dead

### v1 (Alpha)
- made the code actually run
- cleaned up random code segments
- enemies fight back
- `calculateAttack()` does what it was supposed to do
- `time.sleep()` calls here and there for less eyerape
- `coolTransition()` is cleaner
- other shit i forgot about

### v0.1 (Alpha)
- Uploaded initial code