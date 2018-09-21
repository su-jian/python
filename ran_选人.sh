ran_number=$(expr $RANDOM % 6)
echo "大家猜猜本次幸运儿是？？"
sleep 1

case ${ran_number} in
0)
	echo -e "本次幸运儿是\033[31m 邰翀 \033[0m"
;;
1)
	echo -e "本次幸运儿是\033[34m 苏建 \033[0m"
;;
2)
	echo -e "本次幸运儿是\033[35m 王琳琳 \033[0m"
;;
3)
	echo -e "本次幸运儿是\033[36m 王梦莎 \033[0m"
;;
4)
	echo -e "本次幸运儿是\033[5m 仇梓旭 \033[0m"
;;
*)
	echo -e "本次幸运儿是\033[43;32m 吴昊 \033[0m"

esac
