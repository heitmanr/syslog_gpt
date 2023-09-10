# syslog_gpt
Demo only

> [!WARNING]
processing large amounts of data might be costly [my syslog.txt has 128 lines - 1x analysis costs ~25ct]

Learn how to use Chat-GPT to analyze plain-text documents - here Cisco IOS Syslog-Files 

> [!Note]
This is "syslog.py" from https://github.com/automateyournetwork/NetGru/tree/main/chat_with_catalyst
 * credits to John Capobianco

Rewritten to
 * improve
   * readablility of the code
 * add functionality
   * allow the user to interactivly "ask" further questions to demonstrate the "memory" feature

The script acts like a "real" chat-bot now.

## Installation

at least "pip install"
* openai
* chromadb
* langchain
* tiktoken

## Preparation (OpenAI)
* create an OpenAI account
* add billing
  * OpenAI requires to pay initially at least 5USD
  * think about configuring some Quotas to limit your monthly expenes
    * soft-limit(warning)
    * hard-limit(stop (costly) operation)
* create an API Key
* store the Key-Value in your OS
  * Environment Variable called "OPENAI_API_KEY"

## Preparation (syslog.txt)

* log into a Cisco device
* do "show logging"
* capture the output into a local file called "syslog.txt"

## Run

just do
* python syslog_gpt.py

### Example
![syslog_gpt](https://github.com/heitmanr/syslog_gpt/assets/26636908/0288b62d-2acf-42e0-aa35-e003d42549d3)


