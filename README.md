The queue bot takes 6 users into a queue and then shuffles them up into two teams of three players. 
The bot then creates two Discord voice channels, one for the Orange team and one for the Blue team.

This bot has the prefix "!" and has the following commands:

```
**q** = upon a user typing this command, they are added to the queue if the queue has less than six people.
**leave** = upon a user typing this command, they leave the queue if they're in the queue.
**status** = upon a user typing this command, the current users in the queue pop up.
```

**Features:**

Below is a display of queueing, checking the status, and then leaving the queue.

![image](https://user-images.githubusercontent.com/38481385/110364481-d4ec7e00-8011-11eb-9eea-81f1855148cf.png)


Below is a display of the queue being finalized and the teams being created. Also, if you try queueing right when a queue is called, 
you are told to wait a few seconds for the previous queue to reset.

![image](https://user-images.githubusercontent.com/38481385/110364616-fe0d0e80-8011-11eb-9348-fc3361d0da0d.png)


Once the queue is finalized, all players in the queue are sent a message from the bot which contains the lobby info + who the host is 
(the host is responsible for creating the private lobby).

This is a message received if you're not the host but on the blue team. It displays who the host is, what team you're on, as well as the lobby info.
![image](https://user-images.githubusercontent.com/38481385/110364926-61973c00-8012-11eb-866c-270dd900ee12.png)

This is a message received if you're the host and on the blue team.
![image](https://user-images.githubusercontent.com/38481385/110365096-986d5200-8012-11eb-8cf4-68a065fcac00.png)

This is a message received if you're not the host but on the orange team.
![image](https://user-images.githubusercontent.com/38481385/110365157-afac3f80-8012-11eb-9dbc-f36d4ae24cae.png)
