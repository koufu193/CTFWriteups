# three
ghidraでデコンパイルすると以下のようなコードが発見される。
```java
//param_1とparam_2はともに0~7の範囲
int FUN_004012b0(int param_1, int param_2) {
    long uVar1;
    uVar1 = 1L << ((param_2 + param_1 * 8L) & 0x3fL);
    if ((uVar1 & 0xfL) != 0) {
        return 0;
    }
    if ((uVar1 & 0x101030L) != 0) {
        return 1;
    }
    if ((uVar1 & 0xe0c0L) != 0) {
        return 2;
    }
    if ((uVar1 & 0x2060200L) != 0) {
        return 3;
    }
    if ((uVar1 & 0x1c080c00L) != 0) {
        return 4;
    }
    if ((uVar1 & 0xe0e00000L) != 0) {
        return 5;
    }
    if ((uVar1 & 0x2020700000000L) != 0) {
        return 6;
    }
    if ((uVar1 & 0x7800000000L) == 0) {
        if ((uVar1 & 0x301010000000000L) != 0) {
            return 8;
        }
        if ((uVar1 & 0xc040c0000000000L) != 0) {
            return 9;
        }
        if ((uVar1 & 0xf00000000000L) != 0) {
            return 10;
        }
        if ((uVar1 & 0x1038000000000000L) == 0) {
            return -((uVar1 & 0xe080000000000000L) == 0 ? 1 : 0) | 0xc;
        }
        return 0xb;
    }
    return 7;
}
```
そしてそれをparam_1,param_2ともに0~7で変化させると以下のような出力が手に入る。<br>コード:
```java
public static void print(){
    for(int i=0;i<8;i++){
        for(int j=0;j<8;j++){
            System.out.printf("%2d,",FUN_004012b0(i,j));
        }
        System.out.println();
    }
    System.out.println();
}
```
出力
```
 0, 0, 0, 0, 1, 1, 2, 2
-1, 3, 4, 4, 1, 2, 2, 2
-1, 3, 3, 4, 1, 5, 5, 5
-1, 3, 4, 4, 4, 5, 5, 5
 6, 6, 6, 7, 7, 7, 7,-1
 8, 6, 9, 9,10,10,10,10
 8, 6, 9,11,11,11,-1,12
 8, 8, 9, 9,11,12,12,12
```
またデコンパイルすると以下のようなルールをクリアするようなフラグを探せばいいと分かる。
- 左上の0から動き始める
- プレーヤーは上下左右に動ける
- 一度通った地点を通ってはいけない
- 全ての数字を一度は3回連続通らなければならない
- 4回連続同じ数字を通ってはいけない
- 全てのマスを通って左上の0に戻る
- 一番初めは下には動けない
- フラグのフォーマットはdice{[a-z0-9]{32}}

このような条件での解き方を探すと以下のような答えが見つかる。
```
→→↓→↓→→↓
↑↓←↑↓↑←↓
↑→→↑→→↑↓
↑←←←←←↓←
→→→→→↑→↓
↑←↓←←←←↓
→↑→→→↓↑↓
↑←←←←←↑←
```
それを読みやすくすると
```
{RIGHT, RIGHT, DOWN, LEFT, DOWN, RIGHT, RIGHT, UP, UP, RIGHT, DOWN, DOWN, RIGHT, RIGHT, UP, LEFT, UP, RIGHT, RIGHT, DOWN, DOWN, DOWN, LEFT, DOWN, RIGHT, DOWN, DOWN, DOWN, LEFT, UP, UP, LEFT, LEFT, LEFT, LEFT, DOWN, RIGHT, RIGHT, RIGHT, DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, UP, RIGHT, UP, LEFT, UP, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, UP, LEFT, LEFT, LEFT, LEFT,LEFT, UP, UP,UP}
```
となる。<br>
32文字から64個の動きを生み出す方法としては<br>
```java
//unmapはアルファベット,数字について0からの番号にしている(順番はa~z0~9)
final int[] DAT_00404020 = {0x04, 0x07, 0x0b, 0x00, 0x20, 0x09, 0x0d, 0x1c, 0x06, 0x15, 0x0d, 0x0d, 0x05, 0x1f, 0x16, 0x14, 0x03, 0x21, 0x07, 0x22, 0x0e, 0x05, 0x1f, 0x07, 0x17, 0x12, 0x0f, 0x0b, 0x10, 0x09, 0x16, 0x07};
char[] flag=new char[0x20];
char[] actions=new char[0x40];
for (int i = 0; i < 0x20; i++) {
    int iVar2 = (unmap.get(flag[i]) + DAT_00404020[i]) % 0x24;
    actions[i * 2] = iVar2 / 6;
    actions[i * 2 + 1] = iVar2 % 6;
}
```
としてから、<br>
作られた64個の数字(0~5の)にそれぞれ動きを割り当てている。<br>
よってそれを解くようなコードを書けば完成。
