# Guess My Cheese (Part 1)
> Try to decrypt the secret cheese password to prove you're not the imposter!<br>
> Connect to the program on our server: nc verbal-sleep.picoctf.net 60985

あまり好きじゃなかった。実行してみると

<pre>
*******************************************
***             Part 1                  ***
***    The Mystery of the CLONED RAT    ***
*******************************************

The super evil Dr. Lacktoes Inn Tolerant told me he kidnapped my best friend, Squeexy, and replaced him with an evil clone! You look JUST LIKE SQUEEXY, but I'm not sure if you're him or THE CLONE. I've devised a plan to find out if YOU'RE the REAL SQUEEXY! If you're Squeexy, I'll give you the key to the cloning room so you can maul the imposter...

Here's my secret cheese -- if you're Squeexy, you'll be able to guess it:  SWHSIQFW
Hint: The cheeses are top secret and limited edition, so they might look different from cheeses you're used to!
Commands: (g)uess my cheese or (e)ncrypt a cheese
What would you like to do?
</pre>
と出る。ヒントを見ると
> Remember that cipher we devised together Squeexy? The one that incorporates your affinity for linear equations???

らしいので一次関数を用いた変換を行っているのかな～と考える。<br>
チーズの名前は知らないのでGuess My Cheese (Part 2)のcheese_list.txtから復号するときに利用しやすいチーズ(僕はBabybel)を探して、あとは解くだけ。