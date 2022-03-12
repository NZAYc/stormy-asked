# Fentanyl Quest Redux

Fork of the original Fentanyl Quest.
A simple turn-based dungeon explorer, played on your terminal.

## changelog

### v1.5 (Alpha)
- split different portions of code into their own files
- added `inventory[]` to `entity` class
- added `item` class
- added `Ilkhar's migration raft` item
- added config file
- re-added debug mode
- moved initial question into the `if main` portion for less indentation

### v1.4 (Alpha)
- `defaultAttack()` changed the default attack values
- `criticalHit()` added a critical hit system
- finished Kakapoop path :)

### v1.3 (Alpha)    
- `time.sleep()` removed some non needed statements
- `coolTransition() `removed some unnecessary passing in of a delay value
- `entity.defaultAttack()` added a default attack function to the entity class 
- `entity.fastAttack()` added a fast attack function to the entity class
- `entity.hardAttack()` added a hard attack function to the entity class
- `handleFight()` changed if: else: return to an if: return
- `handleFight()` added a check in the handleFight while loop to make sure the player does not attack a dead entity
- `askPlayer()` is now called `getPlayerInput()`
- `entity()` constructor changed to take in less arguments
- `print()` `time.sleep()` replaced with `delayPrint()` in a lot of places
- removed a `break` command that was impossible to run because `sys.exit()` got called a line above it
- changed the order of commands to separate arithmetic from printing
- removed unnecessary setting of the enemy name
- removed an unnecessary import (dataclasses)

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