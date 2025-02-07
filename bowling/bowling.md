# Bowling Game Overview:

* **Game Structure**: Consists of 10 frames.
* **Pins**: Each frame starts with 10 standing pins. Pins are reset after each frame but not between throws in the same frame.
* **Throws**: Players get one or two throws per frame, depending on performance.

### Frame Types:

#### Open frame:

Not all 10 pins are knocked down in two throws.
**Score**: The number of pins knocked down in both throws

#### Spare:

All 10 pins are knocked down in two throws (some in the first, remaining in the second).
**Score**: 10 + number of pins knocked down in the first throw of the next frame.

#### Strike:

All 10 pins are knocked down in the first throw.
In case of a Strike, number of throws in the frame is reduced to one.
**Score**: 10 + number of pins knocked down in the next two throws. If the next throw is also a strike, you wait for the throw after that to determine the score for the first strike.

#### Scoring Summary:

- Open Frame: Score = number of pins knocked down.
- Spare: Score = 10 + pins in the first throw of the next frame.
- Strike: Score = 10 + pins in the next two throws.

#### Special Case of last Frame:

If the player scores a Spare, or Strike in the last frame, then additional fill throws are awarded, one in case or Spare, two in case of a Strike.
**Note**: Even if the player scores spares or strike in the fill throws too, no extra fill balls are awarded in such case.

## Requirements

Write code to keep track of the score of a game of bowling.
It should support two operations:

- `roll(pins : int)` is called each time the player rolls a ball.
  The argument is the number of pins knocked down.
- `score() : int` is called only at the very end of the game.
  It returns the total score for that game.

## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" an error when the scoring or playing rules are not followed. The tests will only pass if you both `raise` the `exception` and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# example when a bonus is attempted with an open frame
raise IndexError("cannot throw bonus with an open tenth frame")

# example when fill balls are invalid
raise ValueError("invalid fill balls")
```

## Source

### Created by

- @aes421

### Contributed to by

- @cmccandless
- @Dog
- @kytrinyx
- @RNeilsen
- @tqa236
- @yawpitch

### Based on

The Bowling Game Kata from UncleBob - https://web.archive.org/web/20221001111000/http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata