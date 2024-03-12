while getopts l:i:b:n:r: module
do
    case "${module}" in
        l)lang_abr=${OPTARG};;
        i)input_file=${OPTARG};;
        b)beam=${OPTARG};;
        n)nbest=${OPTARG};;
        r)rerank=${OPTARG};;
    esac
done

while IFS= read -r line; do
    python3 load_input.py "$line"
    bash interactive.sh $lang_abr 'source/source.txt' $beam $nbest
    python3 generate_result_files_txt.py $lang_abr $rerank
done < $input_file