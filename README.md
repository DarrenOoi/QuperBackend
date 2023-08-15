# Quper
## Folder Structure

```
├── README.md
├── LICENSE.md
├── INSTALL.md
├── src
│   ├── Compliance of disclosure
│   │	├── compliance_of_disclosure.py
│   │       ├── predict_content.py  
│   │       ├── find_subtitle.py
│   │       ├── bys_classifier.pkl
│   │       ├── bys_tf.pkl
│   │	├── pp_example
│   ├── Timeliness
│   │	├── timeline.py
│   ├── Availability
├── ├── <!-- External Link -->
│   │   ├── get_external_link.py
├── ├── <!-- Language Type -->
│       ├── get_language_type.py
│   ├── Readability
│   │	├── readability.py
│   │	├── doubleNeg_obscure_qualifiers.py
│   │	├── main_idea-location.py
│   │	├── pp_example
├── dataset
│   ├── title.csv

```
***Note:*** This tree includes only main files. 

## Description:

Below we describe each main file in our folder below.

### src
#### Compliance of disclosure

```compliance of disclosure.py```: Run this file to obtain the full outputs on the console. Filter out privacy policies with unsupported formats and without subheadings. By default, the privacy policy results generated based on the ```pp_example``` folder will be printed. 

```predict_content.py```: Use trained Bayesian classifier(bys_classifier.pkl) as well as a feature vector transformer (bys_tf.pkl) to predict the presence of subtitles in the privacy policy. Please refer to ```predict_content.md``` for details on how to use it.

```find_subtitle.py```: Detect subtitle tags in the privacy policy document. Please refer to ```find_subtitle.md``` for details on how to use it.

```bys_classifier.pkl```: Train a paragraph-level Bayesian classifier. Please refer to ```paragraph_bayesian.md``` for details on how to use it.

```bys_tf.pkl```: 

```types_pp_processing.py```: Process the data-type paragraph and get a matrix containing 0 and 1. 0 stands for the data type not being collected, while 1 stands for being collected. Please refer to ```type_pp_processing.md``` for details on how to use it.


<!-- csv file description -->
CSV files located in ```dataset/training_data``` are mainly used to train classifiers. They include samples that we manually annotated.   
```title.csv``` ---> used by ```paragraph_bayesian.py``` for paragraph-level training  
```personal_type.csv``` ---> used by ```sentence_bayesian.py``` for sentence-level training  

<!-- pp_example -->
The ```*_example``` folds in ```/dataset``` include some examples of privacy policy documents.  


### Phase 2

```test_case_execution.py```: Send test cases to Alexa simulator and obtain skill execution logs. It takes as input the logs generated by a SkillExplorer-based tester (https://vitas000.github.io/tool/) (see examples in /dataset/SkillExplorer_log), 
feeds test cases and outputs the behavior logs. 

* usage: test_case_execution.py [-h] [--t T] [--c C] [--r R]  
	enter the CATEGORY of test cases you want to send  
    optional arguments:  
        -h, --help  show this help message and exit  
        --t T       execute test cases in TYPE category  
        --c C       execute test cases in CHILDREN category  
        --r R       execute test cases in REGIONS category  

```echo_spider.py```: Interact with Alexa simulator

```SkillExplorer_example_log.xlsx```: Contain the name of SkillExplorer_example_log (see examples in /dataset/SkillExplorer_log_example)

```/example/SkillExplorer_log```: Contain the raw conversation logs with Alexa skills that are generated from a SkillExplorer-based tester (https://vitas000.github.io/tool/)

```cookies```: This folder will be automatically created if ```cookies``` path is not existed. It is used to save cookies required by Alex developer console. To obtain this cookie, please register a developer test account from https://developer.amazon.com. For simplicity, we leave our test account in line 314 of ```test_case_execution.py```. Please replace it with yours if you have one.   
(Note: you need to manully delete ```/cookies/console_cookie7.pkl``` file before generate new cookies)

```/library/chromedriver```: A webdriver that can launch chrome browser

### Phase 3 

```behavior_log_process.py```: Derive behavioral profiles from behavior logs and automatically check violations. 
* input: behavior logs (see examples in /dataset/TYPES_example/behavior_logs), PP processing results (see examples in /dataset/TYPES_example/pp_process_results)
* output: violations cases
* usage: behavior_log_process.py [-h] [--t T] [--c C] [--region REGION] [--retention RETENTION]
	enter the CATEGORY of violation cases you want to check  
	optional arguments:  
        -h, --help            show this help message and exit  
        --t T                 check violations in TYPE category (V1)  
        --c C                 check violations in CHILDREN category (V2)  
        --region REGION       check violations in REGIONS category (V3)  
        --retention RETENTION   check violations in RETENTION category (V4)  

```noncompliance_check.py```: Invoked by ```behavior_log_process.py``` to check violations V1 to V4. 

age_keywords.txt, birthday_keywords.txt, email_keywords.txt, location_keywords.txt, phoneno_keywords.txt, postcode_keywords.txt: Contain the keywords list for corresponding data types

```test_cases.txt```: Contain the test cases.
(Note: all the test cases have been anonymized for the double-blind review.)

```Alexa_response_pattern.txt```: Contain Alexa's common response pattern

CHILDREN_example,
REGIONS_example,
RETENTION_example, 
TYPES_example: Contain corresponding sample behavior logs and sample PP processed results

## Benchmark 
```benchmark```: the data in this folder can reproduce the results in table 7 in our paper.
To run our benchmark experiments, you can change the path in line 199, 200, 234, 239, 244 in ```behavior_log_process.py```.
