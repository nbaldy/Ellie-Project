# Ellie's project
MVP due date: June 1st

Input: speech/audio
Output: speech/audio + character interaction

MVP goals:
* 3 character actions
* Basic response to queries (via chat-bot API)
* Audio output

Libraries/APIs/Programs:
* Speech-to-Text: Google Cloud - chosen for cost, as well as the additional entity recognition and sentiment analysis options.
* Text-to-Speech: Google Cloud - chosen for cost, but may be revisited
* Chat-bot: Chat-GPT
* Art/Character creation: Krita - chosen because I already know how to use it and because it's free
* Character animation: Unity - chosen because it's free and due to the large support/userbase

Most development will occur via a Raspberry Pi 3. The exception is the initial character/unity creation, which will happen in Windows, until I understand the interface well enough to port it to linux (or all development in Windows and just porting the generated interface).

## Setup
```
./install_deps.sh
```
