# Guess My Cheese (Part 2)
> The imposter was able to fool us last time, so we've strengthened our defenses!<br>
> Here's our [list of cheeses.](./cheese_list.txt)<br>
> Connect to the program on our server: nc SERVERPORT

僕はあまり好きじゃなかった。コマンドを実行すると
<pre>
*******************************************
***             Part 2                  ***
***    The Mystery of the CLONED RAT    ***
*******************************************

DRAT! The evil Dr. Lacktoes Inn Tolerant's clone was able to guess the cheese last time! I guess simple ciphers aren't good hashing methods. But now I've strengthened my encryption scheme so that now ONLY SQUEEXY can guess it...

Here's my secret cheese -- if you're Squeexy, you'll be able to guess it:  1ce637fefcbdf33d7cb5dd467f577a5912f8a2818d29880616906fcd45692308

Commands: (g)uess my cheese
What would you like to do?
</pre>
と表示される。Part 1とは違い暗号化もできなさそうだ。<br>
1ce637fefcbdf33d7cb5dd467f577a5912f8a2818d29880616906fcd45692308はSHA-256だと予想したがわからなかったのでヒントを見るとサルトが追加されているらしい。<br>
わからなかったのでChatGPTにあり得る組み合わせ(大文字小文字サルトの位置)を調べるコードを書いてもらって実行してみると 小文字+サルト(一バイト) であることがわかったのであとは総当たり。<br>