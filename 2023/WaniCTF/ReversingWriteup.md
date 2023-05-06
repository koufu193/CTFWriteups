<big>__Just_Passw0rd__</big><br><br>
実行して終了
<br><br>
<big>__javersing__</big><br><br>
解凍してIntelliJとかでコードを見て作り直す<br>
直した結果:
```java
public class Main {
    public static void main(String[] args){
        String var1 = "Fcn_yDlvaGpj_Logi}eias{iaeAm_s";
        char[] flag=new char[30];
        for(int i = 0; i < 30; ++i) {
            flag[i*7%30]=var1.charAt(i);
        }
        System.out.println(flag);
    }
}
```
<br><br>
<big>__fermat__</big><br><br>
フェルマーのやつなので計算誤差を狙うか、コード書き換える<br>
僕はバイナリエディタでした
<br><br>
<big>__theseus__</big><br><br>
変数を外部から変えてるということが分かる<br>
つまりそれに沿ったことをする(コードを別ので書いて)
<br><br>
<big>__web_assembly__</big><br><br>
開いてみると(wasmファイルは通信とか見たらどこにあるかわかる)<br>
最後のほうに文字列が並んでる事が分かるのでユーザー名とパスワードであり得そうなのを探す<br>
最後はユーザー名とパスワードを打っておわり
<br><br><big>__Lua__</big><br><br>
いろんな場所で引数とかをdumpしたら見つかる<br>
参考サイト: https://stackoverflow.com/questions/9168058/how-to-dump-a-table-to-console
