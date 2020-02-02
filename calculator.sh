#!/bin/bash
#if [ $# != 0 ] 
#then
  #echo "usage : $0" ;
  #exit 1
#fi

#adinrec -lv 4000 Signaux_ope/operation.wav
#Bin/reconnaissance Listes/wav.mine.lst Modeles/appris Resultats/

#touch "calc.txt"

#cut -d' ' -f3 Resultats/operation.rec > Resultats/calc.txt
#python myscript.py
#cacl est le fichier de test si le micro ne marche pas
sign=''
grep -Po '(?<=\[SEM=)[^()]*?(?=\])' cacl.txt > res

val1=$(sed '1q;d' res)
#variable used to test if value is a number
re='^[0-60]+$'

if ! [[ $(sed '2q;d' res) =~ $re ]] ; then
   eval sign=$(sed '2q;d' res)
   val2=$(sed '3q;d' res)
else
   val1=`expr $val1 + $(sed '2q;d' res)`
   eval sign=$(sed '3q;d' res)
   val2=$(sed '4q;d' res)
fi
if [[ $(sed '5q;d' res) =~ $re ]] ; then
   val2=`expr $val2 + $(sed '5q;d' res)`
fi

case "$sign" in
   "times")  echo $val1*$val2=`expr $val1 \* $val2`
   ;;
   "add") echo $val1+$val2=`expr $val1 + $val2`
   ;;
   "subtract") echo $val1-$val2=`expr $val1 - $val2`
   ;;
   "divide") echo $val1/$val2=`expr $val1 / $val2`
   ;;
   "power") echo $val1^$val2=`expr $val1 ** $val2`
   ;;
   "modulo") echo $val1%$val2=`expr $val1 % $val2`
   ;;
esac
