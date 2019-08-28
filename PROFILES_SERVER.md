# Supported Features

This file lists the implementation status of conformance units of the stack.
These conformance units can be grouped in:

- Categories
- Conformance Groups
- Profiles and Facets 

In addition the current CTT (Compliance Test Tools) results are given.

## Explanation


The following tables use these signs to indicate the implementation status:
 * Unknown = :grey_question:
 * Not Implemented = :new_moon:
 * Being Implemented = :waning_crescent_moon:
 * Incubating = :last_quarter_moon:
 * Stable = :full_moon:
 * Certified = :heavy_check_mark:

The following tables use these signs to indicate the test results:
 * Error = :x:
 * Warning = :warning:
 * Not Implemented = :heavy_minus_sign:
 * Skipped = :white_circle:
 * Not Supported = :radio_button:
 * OK = :heavy_check_mark:
 * Back Trace = :collision:
 * No test results = :grey_question:

Project Info:
 * Type = ServerProject
 * Profile = Standard
 * Version = 1.3.340.375

## Grouped by Category

| Status | Result   | Category             | Conformance Unit |
|--------|----------|----------------------|------------------|
| :grey_question: | :heavy_minus_sign: | Security |  |
| | | :grey_question: | :heavy_check_mark: Security None |
| | | :grey_question: | :white_circle: Security User Name Password |
| | | :grey_question: | :white_circle: Security Administration - XML Schema |
| | | :grey_question: | :white_circle: Security User X509 |
| | | :grey_question: | :white_circle: Security Certificate Validation |
| | | :grey_question: | :white_circle: Security Certificate Administration |
| | | :grey_question: | :heavy_check_mark: Security None CreateSession ActivateSession |
| | | :grey_question: | :heavy_check_mark: Security None CreateSession ActivateSession 1.01 |
| | | :grey_question: | :heavy_check_mark: Security Basic 128Rsa15 |
| | | :grey_question: | :heavy_check_mark: Security Basic 256Sha256 |
| | | :grey_question: | :heavy_check_mark: Security Administration |
| | | :grey_question: | :heavy_minus_sign: Security - No Application Authentication |
| | | :grey_question: | :heavy_check_mark: Security Basic 256 |
| | | :grey_question: | :white_circle: Security User Anonymous |
| | | :grey_question: | :white_circle: Security User IssuedToken Kerberos |
| | | :grey_question: | :white_circle: Security User IssuedToken Kerberos Windows |
| | | :grey_question: | :heavy_check_mark: Security Encryption Required |
| | | :grey_question: | :heavy_check_mark: Security Signing Required |
| | | :grey_question: | :white_circle: Security Time Synch - Configuration |
| | | :grey_question: | :white_circle: Security Time Synch - NTP/OS Based Support |
| | | :grey_question: | :white_circle: Security Time Synch - UA Based Support |
| | | :grey_question: | :white_circle: Security Default ApplicationInstanceCertificate |
| | | :grey_question: | :white_circle: Security No Application Authentication |
| :grey_question: | :x: | Server |  |
| | | :grey_question: | :heavy_check_mark: Address Space Base |
| | | :grey_question: | :white_circle: Address Space Events |
| | | :grey_question: | :white_circle: Address Space Complex Datatypes |
| | | :grey_question: | :white_circle: Address Space Method |
| | | :grey_question: | :white_circle: Address Space UserWriteMask Multilevel |
| | | :grey_question: | :white_circle: Address Space User Level Security Base |
| | | :grey_question: | :white_circle: Address Space UserWriteAccess |
| | | :grey_question: | :white_circle: Address Space WriteMask |
| | | :grey_question: | :heavy_check_mark: Attribute Read |
| | | :grey_question: | :heavy_check_mark: Attribute Write Index |
| | | :grey_question: | :white_circle: Attribute Write StatusCode & TimeStamp |
| | | :grey_question: | :white_circle: Attribute Alternate Encoding |
| | | :grey_question: | :white_circle: Attribute Read Complex |
| | | :grey_question: | :warning: Attribute Write Values |
| | | :grey_question: | :white_circle: Attribute Write Complex |
| | | :grey_question: | :white_circle: Auditing Base |
| | | :grey_question: | :white_circle: AuditActivateSessionEventType |
| | | :grey_question: | :white_circle: AuditCertificateEventType |
| | | :grey_question: | :white_circle: AuditCreateSessionEventType |
| | | :grey_question: | :white_circle: AuditOpenSecureChannelEventType |
| | | :grey_question: | :white_circle: AuditUpdateEventType |
| | | :grey_question: | :x: Base Info Core Structure |
| | | :grey_question: | :white_circle: Base Info Custom Type System |
| | | :grey_question: | :white_circle: Base Info Diagnostics |
| | | :grey_question: | :white_circle: Base Info Engineering Units |
| | | :grey_question: | :white_circle: Base Info EventQueueOverflowEventType |
| | | :grey_question: | :white_circle: Base Info GetMonitoredItems Method |
| | | :grey_question: | :white_circle: Base Info Model Change |
| | | :grey_question: | :heavy_check_mark: Base Info OptionSet |
| | | :grey_question: | :heavy_check_mark: Base Info Placeholder Modelling Rules |
| | | :grey_question: | :white_circle: Base Info Progress Events |
| | | :grey_question: | :white_circle: Base Info ValueAsText |
| | | :grey_question: | :white_circle: Base Info Property Change |
| | | :grey_question: | :warning: Base Info Server Capabilities |
| | | :grey_question: | :white_circle: Base Info System Status |
| | | :grey_question: | :white_circle: Base Info System Status underlying system |
| | | :grey_question: | :white_circle: Base Info Type System |
| | | :grey_question: | :white_circle: Data Access AnalogItemType |
| | | :grey_question: | :white_circle: Data Access DataItems |
| | | :grey_question: | :white_circle: Data Access MultiState |
| | | :grey_question: | :white_circle: Data Access PercentDeadBand |
| | | :grey_question: | :white_circle: Data Access Semantic Changes |
| | | :grey_question: | :white_circle: Data Access TwoState |
| | | :grey_question: | :white_circle: Data Access ArrayItemType |
| | | :grey_question: | :white_circle: Data Access ComplexNumber |
| | | :grey_question: | :white_circle: Data Access DoubleComplex Number |
| | | :grey_question: | :white_circle: Discovery Get Endpoints |
| | | :grey_question: | :white_circle: Discovery Configuration |
| | | :grey_question: | :white_circle: Discovery Register |
| | | :grey_question: | :white_circle: Discovery Register2 |
| | | :grey_question: | :white_circle: Discovery Accept Registrations |
| | | :grey_question: | :white_circle: Discovery Accept Registrations Security |
| | | :grey_question: | :white_circle: Discovery Find Servers Self |
| | | :grey_question: | :white_circle: Discovery Find Servers Filter |
| | | :grey_question: | :white_circle: Discovery Configuration |
| | | :grey_question: | :heavy_check_mark: Method Call |
| | | :grey_question: | :white_circle: Monitor Alternate Encoding |
| | | :grey_question: | :heavy_check_mark: Monitor Basic |
| | | :grey_question: | :heavy_check_mark: Monitor Items 2 |
| | | :grey_question: | :white_circle: Monitor Items 10 |
| | | :grey_question: | :white_circle: Monitor Items 100 |
| | | :grey_question: | :white_circle: Monitor Items 500 |
| | | :grey_question: | :white_circle: Monitor Items 5000 |
| | | :grey_question: | :heavy_check_mark: Monitor QueueSize_1 |
| | | :grey_question: | :white_circle: Monitor MinQueueSize_02 |
| | | :grey_question: | :white_circle: Monitor MinQueueSize_05 |
| | | :grey_question: | :white_circle: Monitor MinQueueSize_10 |
| | | :grey_question: | :white_circle: Monitor QueueSize_ServerMax |
| | | :grey_question: | :heavy_check_mark: Monitor Value Change |
| | | :grey_question: | :white_circle: Monitor Complex Event Filter |
| | | :grey_question: | :white_circle: Monitor Items Deadband Filter |
| | | :grey_question: | :white_circle: Monitor Triggering |
| | | :grey_question: | :white_circle: Monitor Events |
| | | :grey_question: | :heavy_check_mark: Node Management Delete Ref |
| | | :grey_question: | :heavy_check_mark: Node Management Add Ref |
| | | :grey_question: | :x: Node Management Delete Node |
| | | :grey_question: | :x: Node Management Add Node |
| | | :grey_question: | :white_circle: Protocol Configuration |
| | | :grey_question: | :white_circle: Redundancy Server Transparent |
| | | :grey_question: | :white_circle: Redundancy Server |
| | | :grey_question: | :heavy_check_mark: Session Minimum 1 |
| | | :grey_question: | :heavy_check_mark: Session Minimum 2 Parallel |
| | | :grey_question: | :white_circle: Session Minimum 10 Parallel |
| | | :grey_question: | :white_circle: Session Minimum 50 Parallel |
| | | :grey_question: | :white_circle: Session Minimum 500 Parallel |
| | | :grey_question: | :heavy_check_mark: Session General Service Behaviour |
| | | :grey_question: | :warning: Session Base |
| | | :grey_question: | :white_circle: Session Change User |
| | | :grey_question: | :white_circle: Session Cancel |
| | | :grey_question: | :heavy_check_mark: Subscription Basic |
| | | :grey_question: | :heavy_minus_sign: Subscription Publish Discard Policy |
| | | :grey_question: | :radio_button: Subscription Minimum 1 |
| | | :grey_question: | :white_circle: Subscription Minimum 02 |
| | | :grey_question: | :white_circle: Subscription Minimum 05 |
| | | :grey_question: | :white_circle: Subscription Minimum 10 |
| | | :grey_question: | :heavy_check_mark: Subscription Publish Min 02 |
| | | :grey_question: | :white_circle: Subscription Publish Min 05 |
| | | :grey_question: | :white_circle: Subscription Publish Min 10 |
| | | :grey_question: | :white_circle: Subscription Transfer |
| | | :grey_question: | :white_circle: UserDefinedCU |
| | | :grey_question: | :warning: View Basic |
| | | :grey_question: | :warning: View Minimum Continuation Point 01 |
| | | :grey_question: | :white_circle: View Minimum Continuation Point 05 |
| | | :grey_question: | :white_circle: View Minimum Continuation Point 10 |
| | | :grey_question: | :white_circle: View Minimum Continuation Point 50 |
| | | :grey_question: | :white_circle: View RegisterNodes |
| | | :grey_question: | :heavy_check_mark: View TranslateBrowsePath |
| :grey_question: | :heavy_minus_sign: | Transport |  |
| | | :grey_question: | :white_circle: Protocol Soap Binary WS Security |
| | | :grey_question: | :heavy_minus_sign: Protocol TCP Binary UA Security |
| | | :grey_question: | :white_circle: Protocol Soap Xml WS Security |



## Grouped by Conformance Groups

| Status | Result   | Conformance Group    | Conformance Unit |
|--------|----------|----------------------|------------------|
| :grey_question: | :white_circle: | Address Space Model |  |
| | | :grey_question: | :heavy_check_mark: Address Space Base |
| | | :grey_question: | :white_circle: Address Space Events |
| | | :grey_question: | :white_circle: Address Space Complex Datatypes |
| | | :grey_question: | :white_circle: Address Space Method |
| | | :grey_question: | :white_circle: Address Space UserWriteMask Multilevel |
| | | :grey_question: | :white_circle: Address Space User Level Security Base |
| | | :grey_question: | :white_circle: Address Space UserWriteAccess |
| | | :grey_question: | :white_circle: Address Space WriteMask |
| :grey_question: | :warning: | Attribute Services |  |
| | | :grey_question: | :heavy_check_mark: Attribute Read |
| | | :grey_question: | :heavy_check_mark: Attribute Write Index |
| | | :grey_question: | :white_circle: Attribute Write StatusCode & TimeStamp |
| | | :grey_question: | :white_circle: Attribute Alternate Encoding |
| | | :grey_question: | :white_circle: Attribute Read Complex |
| | | :grey_question: | :warning: Attribute Write Values |
| | | :grey_question: | :white_circle: Attribute Write Complex |
| :grey_question: | :white_circle: | Auditing |  |
| | | :grey_question: | :white_circle: Auditing Base |
| | | :grey_question: | :white_circle: AuditActivateSessionEventType |
| | | :grey_question: | :white_circle: AuditCertificateEventType |
| | | :grey_question: | :white_circle: AuditCreateSessionEventType |
| | | :grey_question: | :white_circle: AuditOpenSecureChannelEventType |
| | | :grey_question: | :white_circle: AuditUpdateEventType |
| :grey_question: | :white_circle: | Base Eventing |  |
| | | :grey_question: | :white_circle: Monitor Events |
| :grey_question: | :x: | Base Information |  |
| | | :grey_question: | :x: Base Info Core Structure |
| | | :grey_question: | :white_circle: Base Info Custom Type System |
| | | :grey_question: | :white_circle: Base Info Diagnostics |
| | | :grey_question: | :white_circle: Base Info Engineering Units |
| | | :grey_question: | :white_circle: Base Info EventQueueOverflowEventType |
| | | :grey_question: | :white_circle: Base Info GetMonitoredItems Method |
| | | :grey_question: | :white_circle: Base Info Model Change |
| | | :grey_question: | :heavy_check_mark: Base Info OptionSet |
| | | :grey_question: | :heavy_check_mark: Base Info Placeholder Modelling Rules |
| | | :grey_question: | :white_circle: Base Info Progress Events |
| | | :grey_question: | :white_circle: Base Info ValueAsText |
| | | :grey_question: | :white_circle: Base Info Property Change |
| | | :grey_question: | :warning: Base Info Server Capabilities |
| | | :grey_question: | :white_circle: Base Info System Status |
| | | :grey_question: | :white_circle: Base Info System Status underlying system |
| | | :grey_question: | :white_circle: Base Info Type System |
| :grey_question: | :white_circle: | Data Access |  |
| | | :grey_question: | :white_circle: Data Access AnalogItemType |
| | | :grey_question: | :white_circle: Data Access DataItems |
| | | :grey_question: | :white_circle: Data Access MultiState |
| | | :grey_question: | :white_circle: Data Access PercentDeadBand |
| | | :grey_question: | :white_circle: Data Access Semantic Changes |
| | | :grey_question: | :white_circle: Data Access TwoState |
| | | :grey_question: | :white_circle: Data Access ArrayItemType |
| | | :grey_question: | :white_circle: Data Access ComplexNumber |
| | | :grey_question: | :white_circle: Data Access DoubleComplex Number |
| :grey_question: | :white_circle: | Discovery Services |  |
| | | :grey_question: | :white_circle: Discovery Get Endpoints |
| | | :grey_question: | :white_circle: Discovery Configuration |
| | | :grey_question: | :white_circle: Discovery Register |
| | | :grey_question: | :white_circle: Discovery Register2 |
| | | :grey_question: | :white_circle: Discovery Accept Registrations |
| | | :grey_question: | :white_circle: Discovery Accept Registrations Security |
| | | :grey_question: | :white_circle: Discovery Find Servers Self |
| | | :grey_question: | :white_circle: Discovery Find Servers Filter |
| | | :grey_question: | :white_circle: Discovery Configuration |
| :grey_question: | :heavy_check_mark: | Method Services |  |
| | | :grey_question: | :heavy_check_mark: Method Call |
| :grey_question: | :white_circle: | Monitored Item Services |  |
| | | :grey_question: | :white_circle: Monitor Alternate Encoding |
| | | :grey_question: | :heavy_check_mark: Monitor Basic |
| | | :grey_question: | :heavy_check_mark: Monitor Items 2 |
| | | :grey_question: | :white_circle: Monitor Items 10 |
| | | :grey_question: | :white_circle: Monitor Items 100 |
| | | :grey_question: | :white_circle: Monitor Items 500 |
| | | :grey_question: | :white_circle: Monitor Items 5000 |
| | | :grey_question: | :heavy_check_mark: Monitor QueueSize_1 |
| | | :grey_question: | :white_circle: Monitor MinQueueSize_02 |
| | | :grey_question: | :white_circle: Monitor MinQueueSize_05 |
| | | :grey_question: | :white_circle: Monitor MinQueueSize_10 |
| | | :grey_question: | :white_circle: Monitor QueueSize_ServerMax |
| | | :grey_question: | :heavy_check_mark: Monitor Value Change |
| | | :grey_question: | :white_circle: Monitor Complex Event Filter |
| | | :grey_question: | :white_circle: Monitor Items Deadband Filter |
| | | :grey_question: | :white_circle: Monitor Triggering |
| | | :grey_question: | :white_circle: Monitor Events |
| :grey_question: | :x: | Node Management Services |  |
| | | :grey_question: | :heavy_check_mark: Node Management Delete Ref |
| | | :grey_question: | :heavy_check_mark: Node Management Add Ref |
| | | :grey_question: | :x: Node Management Delete Node |
| | | :grey_question: | :x: Node Management Add Node |
| :grey_question: | :heavy_minus_sign: | Protocol and Encoding |  |
| | | :grey_question: | :white_circle: Protocol Configuration |
| | | :grey_question: | :white_circle: Protocol Soap Binary WS Security |
| | | :grey_question: | :heavy_minus_sign: Protocol TCP Binary UA Security |
| | | :grey_question: | :white_circle: Protocol Soap Xml WS Security |
| :grey_question: | :white_circle: | Redundancy |  |
| | | :grey_question: | :white_circle: Redundancy Server Transparent |
| | | :grey_question: | :white_circle: Redundancy Server |
| :grey_question: | :heavy_minus_sign: | Security |  |
| | | :grey_question: | :heavy_check_mark: Security None |
| | | :grey_question: | :white_circle: Security User Name Password |
| | | :grey_question: | :white_circle: Security Administration - XML Schema |
| | | :grey_question: | :white_circle: Security User X509 |
| | | :grey_question: | :white_circle: Security Certificate Validation |
| | | :grey_question: | :white_circle: Security Certificate Administration |
| | | :grey_question: | :heavy_check_mark: Security None CreateSession ActivateSession |
| | | :grey_question: | :heavy_check_mark: Security None CreateSession ActivateSession 1.01 |
| | | :grey_question: | :heavy_check_mark: Security Basic 128Rsa15 |
| | | :grey_question: | :heavy_check_mark: Security Basic 256Sha256 |
| | | :grey_question: | :heavy_check_mark: Security Administration |
| | | :grey_question: | :heavy_minus_sign: Security - No Application Authentication |
| | | :grey_question: | :heavy_check_mark: Security Basic 256 |
| | | :grey_question: | :white_circle: Security User Anonymous |
| | | :grey_question: | :white_circle: Security User IssuedToken Kerberos |
| | | :grey_question: | :white_circle: Security User IssuedToken Kerberos Windows |
| | | :grey_question: | :heavy_check_mark: Security Encryption Required |
| | | :grey_question: | :heavy_check_mark: Security Signing Required |
| | | :grey_question: | :white_circle: Security Time Synch - Configuration |
| | | :grey_question: | :white_circle: Security Time Synch - NTP/OS Based Support |
| | | :grey_question: | :white_circle: Security Time Synch - UA Based Support |
| | | :grey_question: | :white_circle: Security Default ApplicationInstanceCertificate |
| | | :grey_question: | :white_circle: Security No Application Authentication |
| :grey_question: | :warning: | Session Services |  |
| | | :grey_question: | :heavy_check_mark: Session Minimum 1 |
| | | :grey_question: | :heavy_check_mark: Session Minimum 2 Parallel |
| | | :grey_question: | :white_circle: Session Minimum 10 Parallel |
| | | :grey_question: | :white_circle: Session Minimum 50 Parallel |
| | | :grey_question: | :white_circle: Session Minimum 500 Parallel |
| | | :grey_question: | :heavy_check_mark: Session General Service Behaviour |
| | | :grey_question: | :warning: Session Base |
| | | :grey_question: | :white_circle: Session Change User |
| | | :grey_question: | :white_circle: Session Cancel |
| :grey_question: | :heavy_minus_sign: | Subscription Services |  |
| | | :grey_question: | :heavy_check_mark: Subscription Basic |
| | | :grey_question: | :heavy_minus_sign: Subscription Publish Discard Policy |
| | | :grey_question: | :radio_button: Subscription Minimum 1 |
| | | :grey_question: | :white_circle: Subscription Minimum 02 |
| | | :grey_question: | :white_circle: Subscription Minimum 05 |
| | | :grey_question: | :white_circle: Subscription Minimum 10 |
| | | :grey_question: | :heavy_check_mark: Subscription Publish Min 02 |
| | | :grey_question: | :white_circle: Subscription Publish Min 05 |
| | | :grey_question: | :white_circle: Subscription Publish Min 10 |
| | | :grey_question: | :white_circle: Subscription Transfer |
| :grey_question: | :white_circle: | UserDefinedCG |  |
| | | :grey_question: | :white_circle: UserDefinedCU |
| :grey_question: | :warning: | View Services |  |
| | | :grey_question: | :warning: View Basic |
| | | :grey_question: | :warning: View Minimum Continuation Point 01 |
| | | :grey_question: | :white_circle: View Minimum Continuation Point 05 |
| | | :grey_question: | :white_circle: View Minimum Continuation Point 10 |
| | | :grey_question: | :white_circle: View Minimum Continuation Point 50 |
| | | :grey_question: | :white_circle: View RegisterNodes |
| | | :grey_question: | :heavy_check_mark: View TranslateBrowsePath |

## Grouped by Profiles and Facets

 Units writen in *italics* are optional within that profile


| Status | Result   | Profile    | Type | Name |
|--------|----------|------------|------|------|
| :grey_question: | :heavy_minus_sign: | Auditing Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Auditing Base |
|  | | :grey_question: | Facet | :heavy_minus_sign:  Standard Event Subscription Server Facet |
| :grey_question: | :white_circle: | Base Server Behaviour Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Protocol Configuration |
|  |  | :grey_question: | Unit | :white_circle: Security Administration - XML Schema |
|  |  | :grey_question: | Unit | :white_circle: Security Certificate Administration |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Administration |
|  |  | :grey_question: | Unit | :white_circle: Discovery Configuration |
| :grey_question: | :white_circle: | Client Redundancy Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Subscription Transfer |
| :grey_question: | :white_circle: | ComplexType Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Monitor Alternate Encoding |
|  |  | :grey_question: | Unit | :white_circle: Attribute Alternate Encoding |
|  |  | :grey_question: | Unit | :white_circle: Attribute Read Complex |
|  |  | :grey_question: | Unit | :white_circle: Address Space Complex Datatypes |
|  |  | :grey_question: | Unit | :white_circle: Attribute Write Complex |
| :grey_question: | :warning: | Core Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :heavy_check_mark: Address Space Base |
|  |  | :grey_question: | Unit | :warning: Base Info Server Capabilities |
|  |  | :grey_question: | Unit | :heavy_check_mark: Base Info Placeholder Modelling Rules |
|  |  | :grey_question: | Unit | :heavy_check_mark: Base Info OptionSet |
|  |  | :grey_question: | Unit | :white_circle: Base Info ValueAsText |
|  |  | :grey_question: | Unit | :heavy_check_mark: Attribute Read |
|  |  | :grey_question: | Unit | :warning: Attribute Write Values |
|  |  | :grey_question: | Unit | :heavy_check_mark: Attribute Write Index |
|  |  | :grey_question: | Unit | :white_circle: Discovery Get Endpoints |
|  |  | :grey_question: | Unit | :white_circle: Discovery Find Servers Self |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Administration |
|  |  | :grey_question: | Unit | :heavy_minus_sign: Security - No Application Authentication |
|  |  | :grey_question: | Unit | :heavy_check_mark: Session General Service Behaviour |
|  |  | :grey_question: | Unit | :warning: Session Base |
|  |  | :grey_question: | Unit | :heavy_check_mark: Session Minimum 1 |
|  |  | :grey_question: | Unit | :warning: View Basic |
|  |  | :grey_question: | Unit | :heavy_check_mark: View TranslateBrowsePath |
|  |  | :grey_question: | Unit | :white_circle: View RegisterNodes |
|  |  | :grey_question: | Unit | :warning: View Minimum Continuation Point 01 |
|  | | :grey_question: | Facet | :white_circle:  User Token - User Name Password Server Facet |
|  | | :grey_question: | Profile | :heavy_check_mark:  SecurityPolicy - None |
| :grey_question: | :white_circle: | DataAccess Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Data Access AnalogItemType |
|  |  | :grey_question: | Unit | :white_circle: Data Access ArrayItemType |
|  |  | :grey_question: | Unit | :white_circle: Data Access ComplexNumber |
|  |  | :grey_question: | Unit | :white_circle: Data Access DataItems |
|  |  | :grey_question: | Unit | :white_circle: Data Access DoubleComplex Number |
|  |  | :grey_question: | Unit | :white_circle: Data Access MultiState |
|  |  | :grey_question: | Unit | :white_circle: Data Access PercentDeadBand |
|  |  | :grey_question: | Unit | :white_circle: Data Access Semantic Changes |
|  |  | :grey_question: | Unit | :white_circle: Data Access TwoState |
| :grey_question: | :heavy_minus_sign: | Embedded DataChange Subscription Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :heavy_check_mark: Monitor Basic |
|  |  | :grey_question: | Unit | :heavy_check_mark: Monitor Value Change |
|  |  | :grey_question: | Unit | :heavy_check_mark: Monitor Items 2 |
|  |  | :grey_question: | Unit | :heavy_check_mark: Monitor QueueSize_1 |
|  |  | :grey_question: | Unit | :heavy_check_mark: Subscription Basic |
|  |  | :grey_question: | Unit | :radio_button: Subscription Minimum 1 |
|  |  | :grey_question: | Unit | :heavy_check_mark: Subscription Publish Min 02 |
|  |  | :grey_question: | Unit | :heavy_minus_sign: Subscription Publish Discard Policy |
| :grey_question: | :x: | Embedded UA Server Profile | Profile |  |
|  |  | :grey_question: | Unit | :x: Base Info Core Structure |
|  |  | :grey_question: | Unit | :white_circle: Base Info Type System |
|  |  | :grey_question: | Unit | :heavy_check_mark: Base Info Placeholder Modelling Rules |
|  |  | :grey_question: | Unit | :white_circle: Base Info Engineering Units |
|  |  | :grey_question: | Unit | :white_circle: Security Default ApplicationInstanceCertificate |
|  | | :grey_question: | Profile | :white_circle:  SecurityPolicy - Basic128Rsa15 |
|  | | :grey_question: | Facet | :heavy_minus_sign:  Standard DataChange Subscription Server Facet |
|  | | :grey_question: | Profile | :warning:  Micro Embedded Device Server |
| :grey_question: | :heavy_minus_sign: | Enhanced DataChange Subscription Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Monitor Items 500 |
|  |  | :grey_question: | Unit | :white_circle: Monitor MinQueueSize_05 |
|  |  | :grey_question: | Unit | :white_circle: Subscription Minimum 05 |
|  |  | :grey_question: | Unit | :white_circle: Subscription Publish Min 10 |
|  | | :grey_question: | Facet | :heavy_minus_sign:  Standard DataChange Subscription Server Facet |
| :grey_question: | :heavy_minus_sign: | Event Subscription Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Monitor Complex Event Filter |
|  |  | :grey_question: | Unit | :heavy_check_mark: Monitor QueueSize_1 |
|  |  | :grey_question: | Unit | :heavy_minus_sign: Subscription Publish Discard Policy |
|  |  | :grey_question: | Unit | :white_circle: Monitor Events |
|  |  | :grey_question: | Unit | :heavy_check_mark: Monitor Basic |
|  |  | :grey_question: | Unit | :white_circle: Monitor Items 10 |
|  |  | :grey_question: | Unit | :white_circle: Subscription Minimum 02 |
|  |  | :grey_question: | Unit | :white_circle: Subscription Publish Min 05 |
|  |  | :grey_question: | Unit | :heavy_check_mark: Subscription Basic |
| :grey_question: | :white_circle: | Method Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :heavy_check_mark: Method Call |
|  |  | :grey_question: | Unit | :white_circle: Address Space Method |
| :grey_question: | :warning: | Micro Embedded Device Server | Profile |  |
|  |  | :grey_question: | Unit | :heavy_check_mark: Session Minimum 2 Parallel |
|  | | :grey_question: | Facet | :heavy_minus_sign:  Embedded DataChange Subscription Server Facet |
|  | | :grey_question: | Profile | :warning:  Nano Embedded Device Server Profile |
| :grey_question: | :warning: | Nano Embedded Device Server Profile | Profile |  |
|  | | :grey_question: | Facet | :warning:  Core Server Facet |
|  | | :grey_question: | Profile | :heavy_minus_sign:  UA-TCP UA-SC UA Binary |
| :grey_question: | :x: | Node Management Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :heavy_check_mark: Node Management Delete Ref |
|  |  | :grey_question: | Unit | :heavy_check_mark: Node Management Add Ref |
|  |  | :grey_question: | Unit | :x: Node Management Delete Node |
|  |  | :grey_question: | Unit | :x: Node Management Add Node |
|  |  | :grey_question: | Unit | :heavy_check_mark: Address Space Base |
| :grey_question: | :white_circle: | Redundancy Transparent Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Redundancy Server Transparent |
| :grey_question: | :white_circle: | Redundancy Visible Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Redundancy Server |
| :grey_question: | :white_circle: | SOAP-HTTP WS-SC UA Binary | Profile |  |
|  |  | :grey_question: | Unit | :white_circle: Protocol Soap Binary WS Security |
| :grey_question: | :white_circle: | SOAP-HTTP WS-SC UA XML | Profile |  |
|  |  | :grey_question: | Unit | :white_circle: Protocol Soap Xml WS Security |
| :grey_question: | :white_circle: | SOAP-HTTP WS-SC UA XML-UA Binary | Profile |  |
|  |  | :grey_question: | Unit | :white_circle: Protocol Soap Binary WS Security |
|  |  | :grey_question: | Unit | :white_circle: Protocol Soap Xml WS Security |
| :grey_question: | :white_circle: | SecurityPolicy - Basic128Rsa15 | Profile |  |
|  |  | :grey_question: | Unit | :white_circle: Security Certificate Validation |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Basic 128Rsa15 |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Encryption Required |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Signing Required |
| :grey_question: | :white_circle: | SecurityPolicy - Basic256 | Profile |  |
|  |  | :grey_question: | Unit | :white_circle: Security Certificate Validation |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Basic 256 |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Encryption Required |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Signing Required |
| :grey_question: | :white_circle: | SecurityPolicy - Basic256Sha256 | Profile |  |
|  |  | :grey_question: | Unit | :white_circle: Security Certificate Validation |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Basic 256Sha256 |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Encryption Required |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security Signing Required |
| :grey_question: | :heavy_check_mark: | SecurityPolicy - None | Profile |  |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security None |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security None CreateSession ActivateSession |
|  |  | :grey_question: | Unit | :heavy_check_mark: Security None CreateSession ActivateSession 1.01 |
| :grey_question: | :heavy_minus_sign: | Standard DataChange Subscription Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :heavy_check_mark: Method Call |
|  |  | :grey_question: | Unit | :white_circle: Monitor Items Deadband Filter |
|  |  | :grey_question: | Unit | :white_circle: Monitor Items 10 |
|  |  | :grey_question: | Unit | :white_circle: Monitor Items 100 |
|  |  | :grey_question: | Unit | :white_circle: Monitor MinQueueSize_02 |
|  |  | :grey_question: | Unit | :white_circle: Monitor Triggering |
|  |  | :grey_question: | Unit | :white_circle: Subscription Minimum 02 |
|  |  | :grey_question: | Unit | :white_circle: Subscription Publish Min 05 |
|  |  | :grey_question: | Unit | :white_circle: Base Info GetMonitoredItems Method |
|  | | :grey_question: | Facet | :heavy_minus_sign:  Embedded DataChange Subscription Server Facet |
| :grey_question: | :heavy_minus_sign: | Standard Event Subscription Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Base Info Progress Events |
|  |  | :grey_question: | Unit | :white_circle: Base Info System Status |
|  |  | :grey_question: | Unit | :white_circle: Base Info Property Change |
|  |  | :grey_question: | Unit | :white_circle: Base Info EventQueueOverflowEventType |
|  |  | :grey_question: | Unit | :heavy_check_mark: Monitor Basic |
|  |  | :grey_question: | Unit | :white_circle: Monitor Items 10 |
|  |  | :grey_question: | Unit | :white_circle: Monitor QueueSize_ServerMax |
|  |  | :grey_question: | Unit | :white_circle: Monitor Events |
|  |  | :grey_question: | Unit | :white_circle: Monitor Complex Event Filter |
|  |  | :grey_question: | Unit | :heavy_check_mark: Subscription Basic |
|  |  | :grey_question: | Unit | :white_circle: Subscription Minimum 02 |
|  |  | :grey_question: | Unit | :white_circle: Subscription Publish Min 05 |
|  |  | :grey_question: | Unit | :heavy_minus_sign: Subscription Publish Discard Policy |
| :grey_question: | :x: | Standard UA Server | Profile |  |
|  |  | :grey_question: | Unit | :white_circle: Base Info Diagnostics |
|  |  | :grey_question: | Unit | :white_circle: Discovery Register |
|  |  | :grey_question: | Unit | :white_circle: Discovery Register2 |
|  |  | :grey_question: | Unit | :white_circle: Session Change User |
|  |  | :grey_question: | Unit | :white_circle: Session Cancel |
|  |  | :grey_question: | Unit | :white_circle: Session Minimum 50 Parallel |
|  |  | :grey_question: | Unit | :white_circle: View Minimum Continuation Point 05 |
|  |  | :grey_question: | Unit | :white_circle: Attribute Write StatusCode & TimeStamp |
|  | | :grey_question: | Facet | :heavy_minus_sign:  Enhanced DataChange Subscription Server Facet |
|  | | :grey_question: | Profile | :x:  Embedded UA Server Profile |
|  | | :grey_question: | Facet | :white_circle:  User Token - X509 Certificate Server Facet |
| :grey_question: | :heavy_minus_sign: | UA-TCP UA-SC UA Binary | Profile |  |
|  |  | :grey_question: | Unit | :heavy_minus_sign: Protocol TCP Binary UA Security |
| :grey_question: | :white_circle: | User Token - User Name Password Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Security User Name Password |
| :grey_question: | :white_circle: | User Token - X509 Certificate Server Facet | Facet |  |
|  |  | :grey_question: | Unit | :white_circle: Security User X509 |


-----------

Thanks for reading.
This file was generated with: https://github.com/open62541/ua-profiles-md

