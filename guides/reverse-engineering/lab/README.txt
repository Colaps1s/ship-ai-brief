# The little mystery box

An original AI Got Weird teaching fixture, 16 October 2026.
This format and its samples were authored for the guide. This is a reproducible
exercise, not evidence that we tested REA or independently decoded an unknown app.

Requires Python 3. No dependencies, installer, network or executable target.
Unzip the archive and open a terminal in the extracted lab folder.

1. Compare samples/a.lbx, b.lbx and c.lbx using xxd or a hex viewer.
2. Write your header/length/number-size hypothesis before opening the parser.
3. Predict what samples/held-out.lbx contains. Then check your prediction:
   python3 inspect_lbx.py samples/held-out.lbx
   Expected: [256, 513, 65535]
4. Run python3 inspect_lbx.py samples/truncated.lbx
   Expected: size does not match count (nonzero exit).

Format: four bytes ASCII LBX1, a 32-bit little-endian item count,
then that many 16-bit little-endian unsigned integers, with no trailing bytes.
Do not use this simple parser as a production file-format library.

MIT License
Copyright (c) 2026 Artem / AI Got Weird
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to
do so, subject to inclusion of this notice and permission notice in all copies
or substantial portions. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY
OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY ARISING FROM THE SOFTWARE OR ITS USE.
