# CTT Results

This file contains the official CTT (Compliance Test Tools) results for the `example` OPC UA Stack.

## Explanation

The following tables use these signs to indicate the test results:
 * Error = :x:
 * Warning = :warning:
 * Not Implemented = :heavy_minus_sign:
 * Skipped = :white_circle:
 * Not Supported = :radio_button:
 * OK = :heavy_check_mark:
 * Back Trace = :collision:

## Summarized Results for tested Conformance Units

Tested with version: `1.3.340.380`

| Result | Conformance Group   | Conformance Unit    |
|--------|---------------------|---------------------|
| :heavy_check_mark: | Address Space Model |  |
| :heavy_check_mark: |  | Address Space Base |
| :heavy_check_mark: |  | Address Space Method |
| :warning: | Attribute Services |  |
| :heavy_check_mark: |  | Attribute Read |
| :heavy_check_mark: |  | Attribute Write Index |
| :warning: |  | Attribute Write Values |
| :warning: | Base Information |  |
| :heavy_minus_sign: |  | Base Info OptionSet |
| :heavy_minus_sign: |  | Base Info Placeholder Modelling Rules |
| :warning: |  | Base Info ValueAsText |
| :warning: |  | Base Info Server Capabilities |
| :white_circle: | Discovery Services |  |
| :white_circle: |  | Discovery Get Endpoints |
| :white_circle: |  | Discovery Find Servers Self |
| :heavy_check_mark: | Method Services |  |
| :heavy_check_mark: |  | Method Call |
| :warning: | Monitored Item Services |  |
| :warning: |  | Monitor Basic |
| :heavy_check_mark: |  | Monitor Items 2 |
| :heavy_check_mark: |  | Monitor QueueSize_1 |
| :heavy_check_mark: |  | Monitor Value Change |
| :white_circle: | Protocol and Encoding |  |
| :white_circle: |  | Protocol TCP Binary UA Security |
| :warning: | Security |  |
| :heavy_check_mark: |  | Security None |
| :warning: |  | Security User Name Password |
| :heavy_check_mark: |  | Security None CreateSession ActivateSession |
| :white_circle: |  | Security None CreateSession ActivateSession 1.01 |
| :heavy_minus_sign: |  | Security Administration |
| :white_circle: |  | Security - No Application Authentication |
| :warning: | Session Services |  |
| :heavy_check_mark: |  | Session Minimum 1 |
| :heavy_check_mark: |  | Session Minimum 2 Parallel |
| :heavy_check_mark: |  | Session General Service Behaviour |
| :warning: |  | Session Base |
| :warning: | Subscription Services |  |
| :white_circle: |  | Subscription Basic |
| :heavy_minus_sign: |  | Subscription Publish Discard Policy |
| :radio_button: |  | Subscription Minimum 1 |
| :warning: |  | Subscription Publish Min 02 |
| :warning: | View Services |  |
| :warning: |  | View Basic |
| :warning: |  | View Minimum Continuation Point 01 |
| :white_circle: |  | View RegisterNodes |
| :heavy_check_mark: |  | View TranslateBrowsePath |



## Results for all Profiles and Facets

Project Info:
 * Type = ServerProject
 * Profile = Standard
 * Version = 1.3.340.375

### Conformance Groups

| Result   | Conformance Group    | Conformance Unit |
|----------|----------------------|------------------|
| :white_circle: | Address Space Model |  |
| :heavy_check_mark: |  | Address Space Base |
| :white_circle: |  | Address Space Events |
| :white_circle: |  | Address Space Complex Datatypes |
| :heavy_check_mark: |  | Address Space Method |
| :white_circle: |  | Address Space UserWriteMask Multilevel |
| :white_circle: |  | Address Space User Level Security Base |
| :white_circle: |  | Address Space UserWriteAccess |
| :white_circle: |  | Address Space WriteMask |
| :warning: | Attribute Services |  |
| :heavy_check_mark: |  | Attribute Read |
| :heavy_check_mark: |  | Attribute Write Index |
| :white_circle: |  | Attribute Write StatusCode & TimeStamp |
| :white_circle: |  | Attribute Alternate Encoding |
| :white_circle: |  | Attribute Read Complex |
| :warning: |  | Attribute Write Values |
| :white_circle: |  | Attribute Write Complex |
| :white_circle: | Auditing |  |
| :white_circle: |  | Auditing Base |
| :white_circle: |  | AuditActivateSessionEventType |
| :white_circle: |  | AuditCertificateEventType |
| :white_circle: |  | AuditCreateSessionEventType |
| :white_circle: |  | AuditOpenSecureChannelEventType |
| :white_circle: |  | AuditUpdateEventType |
| :white_circle: | Base Eventing |  |
| :white_circle: |  | Monitor Events |
| :warning: | Base Information |  |
| :white_circle: |  | Base Info Core Structure |
| :white_circle: |  | Base Info Custom Type System |
| :white_circle: |  | Base Info Diagnostics |
| :white_circle: |  | Base Info Engineering Units |
| :white_circle: |  | Base Info EventQueueOverflowEventType |
| :white_circle: |  | Base Info GetMonitoredItems Method |
| :white_circle: |  | Base Info Model Change |
| :heavy_check_mark: |  | Base Info OptionSet |
| :heavy_check_mark: |  | Base Info Placeholder Modelling Rules |
| :white_circle: |  | Base Info Progress Events |
| :white_circle: |  | Base Info ValueAsText |
| :white_circle: |  | Base Info Property Change |
| :warning: |  | Base Info Server Capabilities |
| :white_circle: |  | Base Info System Status |
| :white_circle: |  | Base Info System Status underlying system |
| :white_circle: |  | Base Info Type System |
| :white_circle: | Data Access |  |
| :white_circle: |  | Data Access AnalogItemType |
| :white_circle: |  | Data Access DataItems |
| :white_circle: |  | Data Access MultiState |
| :white_circle: |  | Data Access PercentDeadBand |
| :white_circle: |  | Data Access Semantic Changes |
| :white_circle: |  | Data Access TwoState |
| :white_circle: |  | Data Access ArrayItemType |
| :white_circle: |  | Data Access ComplexNumber |
| :white_circle: |  | Data Access DoubleComplex Number |
| :white_circle: | Discovery Services |  |
| :white_circle: |  | Discovery Get Endpoints |
| :white_circle: |  | Discovery Configuration |
| :white_circle: |  | Discovery Register |
| :white_circle: |  | Discovery Register2 |
| :white_circle: |  | Discovery Accept Registrations |
| :white_circle: |  | Discovery Accept Registrations Security |
| :white_circle: |  | Discovery Find Servers Self |
| :white_circle: |  | Discovery Find Servers Filter |
| :white_circle: |  | Discovery Configuration |
| :heavy_check_mark: | Method Services |  |
| :heavy_check_mark: |  | Method Call |
| :warning: | Monitored Item Services |  |
| :white_circle: |  | Monitor Alternate Encoding |
| :warning: |  | Monitor Basic |
| :heavy_check_mark: |  | Monitor Items 2 |
| :white_circle: |  | Monitor Items 10 |
| :white_circle: |  | Monitor Items 100 |
| :white_circle: |  | Monitor Items 500 |
| :white_circle: |  | Monitor Items 5000 |
| :heavy_check_mark: |  | Monitor QueueSize_1 |
| :white_circle: |  | Monitor MinQueueSize_02 |
| :white_circle: |  | Monitor MinQueueSize_05 |
| :white_circle: |  | Monitor MinQueueSize_10 |
| :white_circle: |  | Monitor QueueSize_ServerMax |
| :heavy_check_mark: |  | Monitor Value Change |
| :white_circle: |  | Monitor Complex Event Filter |
| :white_circle: |  | Monitor Items Deadband Filter |
| :white_circle: |  | Monitor Triggering |
| :white_circle: |  | Monitor Events |
| :white_circle: | Node Management Services |  |
| :white_circle: |  | Node Management Delete Ref |
| :white_circle: |  | Node Management Add Ref |
| :white_circle: |  | Node Management Delete Node |
| :white_circle: |  | Node Management Add Node |
| :white_circle: | Protocol and Encoding |  |
| :white_circle: |  | Protocol Configuration |
| :white_circle: |  | Protocol Soap Binary WS Security |
| :white_circle: |  | Protocol TCP Binary UA Security |
| :white_circle: |  | Protocol Soap Xml WS Security |
| :white_circle: | Redundancy |  |
| :white_circle: |  | Redundancy Server Transparent |
| :white_circle: |  | Redundancy Server |
| :white_circle: | Security |  |
| :heavy_check_mark: |  | Security None |
| :white_circle: |  | Security User Name Password |
| :white_circle: |  | Security Administration - XML Schema |
| :white_circle: |  | Security User X509 |
| :white_circle: |  | Security Certificate Validation |
| :white_circle: |  | Security Certificate Administration |
| :heavy_check_mark: |  | Security None CreateSession ActivateSession |
| :white_circle: |  | Security None CreateSession ActivateSession 1.01 |
| :white_circle: |  | Security Basic 128Rsa15 |
| :white_circle: |  | Security Basic 256Sha256 |
| :heavy_check_mark: |  | Security Administration |
| :white_circle: |  | Security - No Application Authentication |
| :white_circle: |  | Security Basic 256 |
| :white_circle: |  | Security User Anonymous |
| :white_circle: |  | Security User IssuedToken Kerberos |
| :white_circle: |  | Security User IssuedToken Kerberos Windows |
| :white_circle: |  | Security Encryption Required |
| :white_circle: |  | Security Signing Required |
| :white_circle: |  | Security Time Synch - Configuration |
| :white_circle: |  | Security Time Synch - NTP/OS Based Support |
| :white_circle: |  | Security Time Synch - UA Based Support |
| :white_circle: |  | Security Default ApplicationInstanceCertificate |
| :white_circle: |  | Security No Application Authentication |
| :warning: | Session Services |  |
| :heavy_check_mark: |  | Session Minimum 1 |
| :heavy_check_mark: |  | Session Minimum 2 Parallel |
| :white_circle: |  | Session Minimum 10 Parallel |
| :white_circle: |  | Session Minimum 50 Parallel |
| :white_circle: |  | Session Minimum 500 Parallel |
| :heavy_check_mark: |  | Session General Service Behaviour |
| :warning: |  | Session Base |
| :white_circle: |  | Session Change User |
| :white_circle: |  | Session Cancel |
| :warning: | Subscription Services |  |
| :white_circle: |  | Subscription Basic |
| :white_circle: |  | Subscription Publish Discard Policy |
| :radio_button: |  | Subscription Minimum 1 |
| :white_circle: |  | Subscription Minimum 02 |
| :white_circle: |  | Subscription Minimum 05 |
| :white_circle: |  | Subscription Minimum 10 |
| :warning: |  | Subscription Publish Min 02 |
| :white_circle: |  | Subscription Publish Min 05 |
| :white_circle: |  | Subscription Publish Min 10 |
| :white_circle: |  | Subscription Transfer |
| :white_circle: | UserDefinedCG |  |
| :white_circle: |  | UserDefinedCU |
| :warning: | View Services |  |
| :warning: |  | View Basic |
| :warning: |  | View Minimum Continuation Point 01 |
| :white_circle: |  | View Minimum Continuation Point 05 |
| :white_circle: |  | View Minimum Continuation Point 10 |
| :white_circle: |  | View Minimum Continuation Point 50 |
| :white_circle: |  | View RegisterNodes |
| :heavy_check_mark: |  | View TranslateBrowsePath |

### Profiles and Facets

 Units writen in *italics* are optional within that profile


| Result   | Profile    | Type | Name |
|----------|------------|------|------|
| :warning: | Auditing Server Facet | Facet |  |
| :white_circle: |  | Unit | Auditing Base |
| :warning: |  | Facet | Standard Event Subscription Server Facet |
| :white_circle: | Base Server Behaviour Facet | Facet |  |
| :white_circle: |  | Unit | Protocol Configuration |
| :white_circle: |  | Unit | Security Administration - XML Schema |
| :white_circle: |  | Unit | Security Certificate Administration |
| :heavy_check_mark: |  | Unit | Security Administration |
| :white_circle: |  | Unit | Discovery Configuration |
| :white_circle: | Client Redundancy Facet | Facet |  |
| :white_circle: |  | Unit | Subscription Transfer |
| :white_circle: | ComplexType Server Facet | Facet |  |
| :white_circle: |  | Unit | Monitor Alternate Encoding |
| :white_circle: |  | Unit | Attribute Alternate Encoding |
| :white_circle: |  | Unit | Attribute Read Complex |
| :white_circle: |  | Unit | Address Space Complex Datatypes |
| :white_circle: |  | Unit | Attribute Write Complex |
| :warning: | Core Server Facet | Facet |  |
| :heavy_check_mark: |  | Unit | Address Space Base |
| :warning: |  | Unit | Base Info Server Capabilities |
| :heavy_check_mark: |  | Unit | Base Info Placeholder Modelling Rules |
| :heavy_check_mark: |  | Unit | Base Info OptionSet |
| :white_circle: |  | Unit | Base Info ValueAsText |
| :heavy_check_mark: |  | Unit | Attribute Read |
| :warning: |  | Unit | Attribute Write Values |
| :heavy_check_mark: |  | Unit | Attribute Write Index |
| :white_circle: |  | Unit | Discovery Get Endpoints |
| :white_circle: |  | Unit | Discovery Find Servers Self |
| :heavy_check_mark: |  | Unit | Security Administration |
| :white_circle: |  | Unit | Security - No Application Authentication |
| :heavy_check_mark: |  | Unit | Session General Service Behaviour |
| :warning: |  | Unit | Session Base |
| :heavy_check_mark: |  | Unit | Session Minimum 1 |
| :warning: |  | Unit | View Basic |
| :heavy_check_mark: |  | Unit | View TranslateBrowsePath |
| :white_circle: |  | Unit | View RegisterNodes |
| :warning: |  | Unit | View Minimum Continuation Point 01 |
| :white_circle: |  | Facet | User Token - User Name Password Server Facet |
| :white_circle: |  | Profile | SecurityPolicy - None |
| :white_circle: | DataAccess Server Facet | Facet |  |
| :white_circle: |  | Unit | Data Access AnalogItemType |
| :white_circle: |  | Unit | Data Access ArrayItemType |
| :white_circle: |  | Unit | Data Access ComplexNumber |
| :white_circle: |  | Unit | Data Access DataItems |
| :white_circle: |  | Unit | Data Access DoubleComplex Number |
| :white_circle: |  | Unit | Data Access MultiState |
| :white_circle: |  | Unit | Data Access PercentDeadBand |
| :white_circle: |  | Unit | Data Access Semantic Changes |
| :white_circle: |  | Unit | Data Access TwoState |
| :warning: | Embedded DataChange Subscription Server Facet | Facet |  |
| :warning: |  | Unit | Monitor Basic |
| :heavy_check_mark: |  | Unit | Monitor Value Change |
| :heavy_check_mark: |  | Unit | Monitor Items 2 |
| :heavy_check_mark: |  | Unit | Monitor QueueSize_1 |
| :white_circle: |  | Unit | Subscription Basic |
| :radio_button: |  | Unit | Subscription Minimum 1 |
| :warning: |  | Unit | Subscription Publish Min 02 |
| :white_circle: |  | Unit | Subscription Publish Discard Policy |
| :warning: | Embedded UA Server Profile | Profile |  |
| :white_circle: |  | Unit | Base Info Core Structure |
| :white_circle: |  | Unit | Base Info Type System |
| :heavy_check_mark: |  | Unit | Base Info Placeholder Modelling Rules |
| :white_circle: |  | Unit | Base Info Engineering Units |
| :white_circle: |  | Unit | Security Default ApplicationInstanceCertificate |
| :white_circle: |  | Profile | SecurityPolicy - Basic128Rsa15 |
| :warning: |  | Facet | Standard DataChange Subscription Server Facet |
| :warning: |  | Profile | Micro Embedded Device Server |
| :warning: | Enhanced DataChange Subscription Server Facet | Facet |  |
| :white_circle: |  | Unit | Monitor Items 500 |
| :white_circle: |  | Unit | Monitor MinQueueSize_05 |
| :white_circle: |  | Unit | Subscription Minimum 05 |
| :white_circle: |  | Unit | Subscription Publish Min 10 |
| :warning: |  | Facet | Standard DataChange Subscription Server Facet |
| :warning: | Event Subscription Server Facet | Facet |  |
| :white_circle: |  | Unit | Monitor Complex Event Filter |
| :heavy_check_mark: |  | Unit | Monitor QueueSize_1 |
| :white_circle: |  | Unit | Subscription Publish Discard Policy |
| :white_circle: |  | Unit | Monitor Events |
| :warning: |  | Unit | Monitor Basic |
| :white_circle: |  | Unit | Monitor Items 10 |
| :white_circle: |  | Unit | Subscription Minimum 02 |
| :white_circle: |  | Unit | Subscription Publish Min 05 |
| :white_circle: |  | Unit | Subscription Basic |
| :heavy_check_mark: | Method Server Facet | Facet |  |
| :heavy_check_mark: |  | Unit | Method Call |
| :heavy_check_mark: |  | Unit | Address Space Method |
| :warning: | Micro Embedded Device Server | Profile |  |
| :heavy_check_mark: |  | Unit | Session Minimum 2 Parallel |
| :warning: |  | Facet | Embedded DataChange Subscription Server Facet |
| :warning: |  | Profile | Nano Embedded Device Server Profile |
| :warning: | Nano Embedded Device Server Profile | Profile |  |
| :warning: |  | Facet | Core Server Facet |
| :white_circle: |  | Profile | UA-TCP UA-SC UA Binary |
| :white_circle: | Node Management Server Facet | Facet |  |
| :white_circle: |  | Unit | Node Management Delete Ref |
| :white_circle: |  | Unit | Node Management Add Ref |
| :white_circle: |  | Unit | Node Management Delete Node |
| :white_circle: |  | Unit | Node Management Add Node |
| :heavy_check_mark: |  | Unit | Address Space Base |
| :white_circle: | Redundancy Transparent Server Facet | Facet |  |
| :white_circle: |  | Unit | Redundancy Server Transparent |
| :white_circle: | Redundancy Visible Server Facet | Facet |  |
| :white_circle: |  | Unit | Redundancy Server |
| :white_circle: | SOAP-HTTP WS-SC UA Binary | Profile |  |
| :white_circle: |  | Unit | Protocol Soap Binary WS Security |
| :white_circle: | SOAP-HTTP WS-SC UA XML | Profile |  |
| :white_circle: |  | Unit | Protocol Soap Xml WS Security |
| :white_circle: | SOAP-HTTP WS-SC UA XML-UA Binary | Profile |  |
| :white_circle: |  | Unit | Protocol Soap Binary WS Security |
| :white_circle: |  | Unit | Protocol Soap Xml WS Security |
| :white_circle: | SecurityPolicy - Basic128Rsa15 | Profile |  |
| :white_circle: |  | Unit | Security Certificate Validation |
| :white_circle: |  | Unit | Security Basic 128Rsa15 |
| :white_circle: |  | Unit | Security Encryption Required |
| :white_circle: |  | Unit | Security Signing Required |
| :white_circle: | SecurityPolicy - Basic256 | Profile |  |
| :white_circle: |  | Unit | Security Certificate Validation |
| :white_circle: |  | Unit | Security Basic 256 |
| :white_circle: |  | Unit | Security Encryption Required |
| :white_circle: |  | Unit | Security Signing Required |
| :white_circle: | SecurityPolicy - Basic256Sha256 | Profile |  |
| :white_circle: |  | Unit | Security Certificate Validation |
| :white_circle: |  | Unit | Security Basic 256Sha256 |
| :white_circle: |  | Unit | Security Encryption Required |
| :white_circle: |  | Unit | Security Signing Required |
| :white_circle: | SecurityPolicy - None | Profile |  |
| :heavy_check_mark: |  | Unit | Security None |
| :heavy_check_mark: |  | Unit | Security None CreateSession ActivateSession |
| :white_circle: |  | Unit | Security None CreateSession ActivateSession 1.01 |
| :warning: | Standard DataChange Subscription Server Facet | Facet |  |
| :heavy_check_mark: |  | Unit | Method Call |
| :white_circle: |  | Unit | Monitor Items Deadband Filter |
| :white_circle: |  | Unit | Monitor Items 10 |
| :white_circle: |  | Unit | Monitor Items 100 |
| :white_circle: |  | Unit | Monitor MinQueueSize_02 |
| :white_circle: |  | Unit | Monitor Triggering |
| :white_circle: |  | Unit | Subscription Minimum 02 |
| :white_circle: |  | Unit | Subscription Publish Min 05 |
| :white_circle: |  | Unit | Base Info GetMonitoredItems Method |
| :warning: |  | Facet | Embedded DataChange Subscription Server Facet |
| :warning: | Standard Event Subscription Server Facet | Facet |  |
| :white_circle: |  | Unit | Base Info Progress Events |
| :white_circle: |  | Unit | Base Info System Status |
| :white_circle: |  | Unit | Base Info Property Change |
| :white_circle: |  | Unit | Base Info EventQueueOverflowEventType |
| :warning: |  | Unit | Monitor Basic |
| :white_circle: |  | Unit | Monitor Items 10 |
| :white_circle: |  | Unit | Monitor QueueSize_ServerMax |
| :white_circle: |  | Unit | Monitor Events |
| :white_circle: |  | Unit | Monitor Complex Event Filter |
| :white_circle: |  | Unit | Subscription Basic |
| :white_circle: |  | Unit | Subscription Minimum 02 |
| :white_circle: |  | Unit | Subscription Publish Min 05 |
| :white_circle: |  | Unit | Subscription Publish Discard Policy |
| :warning: | Standard UA Server | Profile |  |
| :white_circle: |  | Unit | Base Info Diagnostics |
| :white_circle: |  | Unit | Discovery Register |
| :white_circle: |  | Unit | Discovery Register2 |
| :white_circle: |  | Unit | Session Change User |
| :white_circle: |  | Unit | Session Cancel |
| :white_circle: |  | Unit | Session Minimum 50 Parallel |
| :white_circle: |  | Unit | View Minimum Continuation Point 05 |
| :white_circle: |  | Unit | Attribute Write StatusCode & TimeStamp |
| :warning: |  | Facet | Enhanced DataChange Subscription Server Facet |
| :warning: |  | Profile | Embedded UA Server Profile |
| :white_circle: |  | Facet | User Token - X509 Certificate Server Facet |
| :white_circle: | UA-TCP UA-SC UA Binary | Profile |  |
| :white_circle: |  | Unit | Protocol TCP Binary UA Security |
| :white_circle: | User Token - User Name Password Server Facet | Facet |  |
| :white_circle: |  | Unit | Security User Name Password |
| :white_circle: | User Token - X509 Certificate Server Facet | Facet |  |
| :white_circle: |  | Unit | Security User X509 |


-----------

Thanks for reading.
This file was generated with: https://github.com/open62541/ua-profiles-md

