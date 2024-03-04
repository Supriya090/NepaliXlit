# Nepali Transliteration

**Adaptation of [IndicXlit](https://github.com/AI4Bharat/IndicXlit) for Nepali systems.**

<hr>

Follow the instructions to run it on your system

1. Install the necessary libraries

    ```
    pip3 install sacremoses torch==2.2.0 pandas mock sacrebleu tensorboardX pyarrow indic-nlp-library xformers triton gdown
    ```

2. Install fairseq from source
    
    ```
    git clone https://github.com/pytorch/fairseq.git
    cd fairseq

    pip install --editable ./
    cd ..
    ```


3. Clone the NepaliXlit repository (to setup and run command line inference)

    ```
    c
    cd NepaliXlit
    ```


4. Download the models
    ```
    # Download nepalixlit
    gdown 1v0RQU9BMhQJNzsesp_2BN1sImCbdw77d --output nepalixlit-en-ne.zip
    unzip nepalixlit-en-ne.zip

    # download the Unigram dictionaries for reranking from IndixXlit github release
    wget https://github.com/AI4Bharat/IndicXlit/releases/download/v1.0/word_prob_dicts.zip
    unzip word_prob_dicts.zip
    ```


5. Creating the dir for saving input and output files

    ```
    mkdir source 
    mkdir output
    ```

6. Saving the input words to source file

    ```
    echo "namaste k xa haalkhabar" >> source/input.txt
    ```

7. Running the inference script

    ```
    # -l = language code :: str
    # -i = name of the input file :: str
    # -b = beam size :: int
    # -n = best n candidates (b>=n) :: int
    # -r = rerank :: boolean (1 or 0)
    bash transliterate_sentence.sh -l 'ne' -i 'source/input.txt' -b 5 -n 5 -r 1

    ```

8. Display the output 

    ```
    cat output/final_transliteration.txt
    ```
