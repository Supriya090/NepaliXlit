# Nepali Transliteration

**Adaptation of [IndicXlit](https://github.com/AI4Bharat/IndicXlit) for Nepali systems.**

<hr>

Follow the instructions to run it on your system

1. Installation

    ```
    ## Install the necessary libraries
    pip3 install sacremoses pandas mock sacrebleu tensorboardX pyarrow indic-nlp-library xformers triton
    pip3 install indic-nlp-library

    ## Install fairseq from source
    git clone https://github.com/pytorch/fairseq.git
    cd fairseq

    pip install --editable ./
    cd ..
    ```


2. Clone the NepaliXlit repository (to setup and run command line inference)

    ```
    git clone https://github.com/Supriya090/NepaliXlit.git
    cd NepaliXlit
    ```


3. Download the models
    ```
    # Download nepalixlit
    gdown 1v0RQU9BMhQJNzsesp_2BN1sImCbdw77d --output nepalixlit-en-ne.zip
    unzip nepalixlit-en-ne.zip

    # download the Unigram dictionaries for reranking from IndixXlit github release
    wget https://github.com/AI4Bharat/IndicXlit/releases/download/v1.0/word_prob_dicts.zip
    unzip word_prob_dicts.zip
    ```


4. Creating the dir for saving input and output files

    ```
    mkdir source 
    mkdir output
    ```

5. Saving the input words to source file

    ```
    echo "namaste k xa haalkhabar" >> source/input.txt
    ```

6. Running the inference script

    ```
    # -l = language code :: str
    # -i = name of the input file :: str
    # -b = beam size :: int
    # -n = best n candidates (b>=n) :: int
    # -r = rerank :: boolean (1 or 0)
    bash transliterate_word.sh -l 'ne' -i 'source/input.txt' -b 5 -n 5 -r 1

    ```

7. Display the output 

    ```
    cat output/final_transliteration.txt
    ```
