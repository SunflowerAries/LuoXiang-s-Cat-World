
# LuoXiang's Cat World

<div align="center">
    <img src="README/logo.ico" style="zoom:40%">
</div>

### Introduction

This is a project for Introduction to Database Systems(COMP130010.01) @Fudan University, a web game for pet cat raising.

---

### Roles you will play

Here are two roles you can choose: **cat master** and **market manager**.

#### A cat master 

Cat masters are the center of this game. You should have a game name and password to login the game (always choose to login as MASTER). You can register a new account if you will. Then, we will have start-up money and nothing else. 

##### Things you can do as a cat master

- Feed the cats

  The main goal for cat masters is to adopt many lovely cats in the parks. You can buy food from the market and feed the stray cats in park. To some point, the cat may beg you to adopt it and give it a lovely name, and surely you can also turn it down. After that, you will find a nice cat stay in you home page. 

- Buy and sell food

  There are different markets which have different price even for the same products. You can use you money to buy food and sell some food to the markets to earn money.

- Have a conversation with markets

  You might be not satisfied with the prices or kinds of the food markets supply and wish for a chance to take to the managers. And the solution is simple. Go the market and just leave a message, the managers of this market will see this and give a reply.  (Only you and this manager can see this message.) 

- Use the cat filter to search cats in all parks or in a specific park.

##### Some hints for a cat master

- *How to earn money?* You can make money by reselling the food in the markets, since the prices may fluctuate and different stores may have varied prices for the goods,  then you can make big profits or lose your shirt. it's just like stocks, isn't it?

- *The status of cats*. You may find that the cat has different status: 

  - A LITTLE HUNGRY
  - PRETTY HUNGRY NOW!
  - STARVING TO DEATH!

  The cat will become more hungry with the passage of time. You may understand the meaning of the status and what will happen to different status intuitively. The hint here is that the status matters!

- *Effects of food*. As different foods have varied prices, it's obvious that every kind of foods has different effects on the cats. 


#### A market manager

Being a manager is much easier than being a cat master. A manager is a pivot for running a market.

##### Thing you can do as a market manager

- You have the power to change the prices of food directly
- Put food into the market or move some food out. 
- Have conversations with cat master. They may bargain with you or just start some free talks. Being polite is important. :-)
- Ads new arrival by using the conversation function.

##### Some hints for a market manager

- Remember there might more than one manager for a market, so your decision may not work. 
- For manager, you can set the prices of the goods in your stores and have conversations with the master, topics may include but not limited to the following ones:
  - Bargaining
  - Ads new arrival

---

#### Be careful!

Because some special reasons, the frequent refresh of the page will cause unexcepted results. We sincerely recommend you to jump to different pages to have a look rather than refreshing a single page and waiting for a wonder to happen. :-)

---

## As a *CatGod*

Information above is a respective of a play, but for a super manager who hold the game should do the following things to start up. 

- Dependencies (test on Windows):

  - Python
  - Django

- Migrate the database by 

  `python manage.py migrate`

- Create a super user

  `python manage.py createsuperuser`

- Go into the local admin page of Django to have some settings of parks and markets (Also their managers).  The cat can be produced automatically. 

---

This work is done by [@Josep-h](https://github.com/Josep-h) and [@SunflowerAries](https://github.com/SunflowerAries). Please feel free to contact us if you have some nice ideas. 