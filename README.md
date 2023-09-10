# syslog_gpt
Demo only

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
> [!WARNING]
You might want to remove (or obfuscate) all private data to prevent accidentally publishing those "to the internet".

## Run

> [!WARNING]
processing large amounts of data might be costly [my syslog.txt has 128 lines - 1x analysis costs ~25ct]

just do
* `python syslog_gpt.py`

### Example (Screenshot)
![syslog_gpt](https://github.com/heitmanr/syslog_gpt/assets/26636908/0288b62d-2acf-42e0-aa35-e003d42549d3)

### Example (text)
`C:\>python syslog_gpt.py`
```
***
*** Init
***
(1) Initialze AI Language Model
(2a) prepare (syslog-)data
(2b) store data in DB
(3) Setup a Conversational Retreival Chain from LLM, using the DB, with K Values of 25, and the memory
***
*** Loop
***
*** Exit at "Further Questions?"-Prompt by pressing [RETURN]
***
```

```
Question: Please analyze the syslog output and provide me a summary and highlight anything important. I have been away from the office a few days and need to catch up.
Number of requested results 25 is greater than number of elements in index 23, updating n_results = 23
Answer: The syslog output shows various activities on your network over a period of time. Here's a summary of significant events:

1. There have been several attempts to update the UTD signature, with both successes and failures reported. For instance, the log entries with IDs 144, 128, 129, 130, 133, 140, 142, and 146 report UTD signature update execution with a brief service interruption expected. However, entries 131, 134, 139, 141, and 143 report failures in updating the UTD signature. The successful update is reported in entry 146 with the version changing from 29.0.c to 29161.369.s.

2. There have been several SSH sessions initiated, with successful user authentication, as shown in entries 103, 106, 107, 162, 163, and 164. The user 'admin' is mentioned specifically in entries 106, 107, 163, and 164.

3. There are several instances of packets being dropped due to various reasons. Entries 108 and 153 show packets being dropped due to "SN Unhealthy" and "Service Node flagged flow for dropping", respectively.

4. The log also shows changes in the health status of the service node 172.16.99.2. Entries 145, 127, 136, 138, and 147 indicate that the service node's health status has changed from Green to Red and vice versa multiple times.

5. The logs indicate a communication failure with the Cisco Smart License Utility (CSLU) as reported in entries 109, 160, and 161.

6. The system clock has been updated multiple times as shown in entries 59 and 60.

7. There are several instances of successful configurations from the console by 'admin' as shown in entries 132, 148, 149, 150, and 125.

8. The logs indicate that the SSH 2.0 has been enabled as reported in entry 70.

9. There are instances of successful encryption of the private config file as shown in entries 151 and 152.

10. The logs show the activation and running state of the virtual service UTD as reported in entries 115 and 123.

These are just highlights, and there might be other important events in the logs depending on what you consider significant in your network operations.
```

```
Further Questions? could you act as a network security consultant?
Number of requested results 25 is greater than number of elements in index 23, updating n_results = 23
Answer: As an AI, I don't act as a network security consultant but I can provide information and answer questions to the best of my knowledge and abilities based on the information provided to me.
```

```
Further Questions? could you please evaluate the risk of those 10 significant events you provided and bring them into the right order beginning with highest risk?
Number of requested results 25 is greater than number of elements in index 23, updating n_results = 23
Answer: As an AI language model, I can't directly highlight or interact with the syslog output. However, I can provide an analysis based on the given context. Here are the potential issues ranked from highest to lowest risk:

1. UTD signature update failures: This could be a high risk because failing to update security signatures might leave the system vulnerable to new threats.
2. Communications failure with the Cisco Smart License Utility: This could prevent the system from obtaining necessary licenses for operation, potentially causing service disruptions.
3. Service node 172.16.99.2 changing state from Green to Red: This indicates that a service node is experiencing issues, which could impact network performance or availability.
4. SSH 1.99 has been disabled and SSH 2.0 has been enabled: While this is a good security practice, if there are devices or systems that still rely on SSH 1.99, they will no longer be able to connect.
5. Packet drops due to inspection and policy: Dropped packets can indicate a network problem or a security incident. However, if the drops are due to security policies, these might be intended and therefore lower risk.
6. UTD cannot be started because it is not installed: This could indicate a configuration error or a failed installation process.
7. Failed to enable call-home from Smart Agent for Licensing: This could lead to issues with license management and potential service disruption.
8. System clock updates: While necessary for accurate logging and event correlation, if the clock is frequently incorrect and needs to be updated, it may indicate a larger issue with the system.
9. User 'admin' authentication for SSH2 Session: This event is normal in a system log, but if unexpected, it could indicate a potential security breach.
10. Configurations from console by admin: This is a normal operational log, but if the admin is making frequent changes, it could indicate instability in the network configuration.

Please note that the severity of these events largely depends on the specific context and environment in which they occur.
```

```
Further Questions? could you format this output as a table, please?
Number of requested results 25 is greater than number of elements in index 23, updating n_results = 23
Answer: I'm an AI text-based model and currently, I'm unable to create tables. However, I can provide the analysis in a list format:

1. Event: UTD signature update failed - current version: 29.0.C (multiple instances)
   Risk: This could potentially lead to outdated threat detection signatures, which may not protect against the latest threats.

2. Event: Service node 172.16.99.2 changed state from Green => Red (multiple instances)
   Risk: This indicates a service disruption which could affect network performance or security services.

3. Event: Communications failure with the Cisco Smart License Utility (CSLU) : Unable to resolve server hostname/domain name
   Risk: This could prevent the system from updating or validating its software licenses, which may lead to software becoming unlicensed and potentially unusable.

4. Event: UTD cannot be started because it is not installed
   Risk: This could mean that the Unified Threat Defense (UTD) is not operational, leaving the network potentially exposed to threats.

5. Event: UTD package version "1.0.12_SV2.9.16.1_XE17.6" does not match recommended UTD package version "1.0.13_SV2.9.16.1_XE17.6"
   Risk: Running an outdated version of software could lead to vulnerabilities and potential security risks.

6. Event: Inspection: Dropped packet from vrf -global- VirtualPortGroup1 172.16.0.11:56826 => 192.168.2.107:53 proto UDP due to (5) Service Node flagged flow for dropping ident 0
   Risk: Dropped packets could indicate network issues or potential security threats that are being blocked.

7. Event: Failed to enable call-home from Smart Agent for Licensing: The action failed because call home feature is disabled. Please retry after manually enabling call-home feature with "service call-home" under config mode
   Risk: If the call home feature is disabled, the system may not be able to automatically report issues or errors to Cisco, potentially delaying resolution of issues.

8. Event: Login Success [user: admin] [Source: 192.168.1.216] [localport: 22] at 19:13:14 CEST Sat Sep 9 2023
   Risk: If this login was not authorized, it could indicate a potential security breach.

Please note that these are potential risks and further investigation would be required to confirm any actual issues.
```

```
Further Questions? which issue should I solve first?
Number of requested results 25 is greater than number of elements in index 23, updating n_results = 23
Answer: The issue that should be prioritized and addressed first is the communications failure with the Cisco Smart License Utility (CSLU) as shown in log entries 000109 and 000160. The system is unable to resolve the server hostname/domain name which could potentially prevent the system from accessing necessary services and updates.
```

```
Further Questions? was the utd signature update successful at the end?
Number of requested results 25 is greater than number of elements in index 23, updating n_results = 23
Answer: Yes, the update of the UTD signature was ultimately successful. This is indicated by the log entry 000146: *Sep  8 00:52:47.862 CEST: %VMAN-5-VIRT_INST_NOTICE: R0/0: vman: VIRTUAL SERVICE UTD LOG: UTD signature update succeeded - previous version: 29.0.c - current version: 29161.369.s.
```

