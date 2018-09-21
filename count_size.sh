#!bin/bash

#指定目录下面文件占用空间大小超过10M的文件的数目和大小总和

read -p "请输入需要统计的目录：" dir_path
read -p "请输入需要统计文件大小(2M/200K)：" file_size
file_array=($(find ${dir_path} ! -type d -a -size +${file_size} | tr "\n" " "))

for i in ${!file_array[@]}
do
    file_s=$(du ${file_array[$i]} | cut -f1)
    echo -e "超过${file_size}的文件有${file_array[$i]}\n文件大小：$((file_s/1024 ))M"
    ((total_size=file_s+total_size))
done

echo -e "超过${file_size}的文件数目: ${#file_array[@]}\n这些文件的总大小是: $((total_size/1024 ))M"
