import sys
import chatbomb

if len(sys.argv) < 3:
    print("Usage: run.py <4 letter game code> \"<text>\" <bot amount: optional> <element timeout: optional>\n<bot amount> default: 5\n<element timeout> default: 60")
else:
    if len(sys.argv) == 3:
        chatbomb.chatbomb(sys.argv[1], sys.argv[2], 5, 60)
    if len(sys.argv) == 4:
        chatbomb.chatbomb(sys.argv[1], sys.argv[2], int(sys.argv[3]), 60)
    if len(sys.argv) >= 5:
        chatbomb.chatbomb(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
