# KFS Software Engineer Coding Exercise

This document outlines the coding exercise as part of the NetApp Keystone Software Engineer interview process.

## Background

NetApp ONTAP is a software solution for managing data on deployed servers in a performant and secure manner. As a Keystone Engineer, part of our role involves collecting and aggregating data from ONTAP instances for upstream processes. Cloud Volumes ONTAP (CVO) is a virtual machine-based instance of ONTAP that provides similar functionality but strictly for cloud usage. For this exercise you have been provided access to a test CVO and it's API, and will be expected to collect, aggregate and present a small amount of data.

## Objective

Create a RESTful API which returns a list of ONTAP Volumes found on the provided CVO. These Volumes should have the following fields returned:

-   Volume UUID
-   Volume Name 
-   Volume State
-   IOPS Density 

Where IOPS Density can be calculated as:

```
IOPS Density = Maximum IOPS / Volume Size (GiB)
```

If a Volume has a QoS Policy set, the Maximum IOPS is it's Max Throughput IOPS. Otherwise use the sum of the Total Raw IOPS Statistic of its Aggregates<sup>*</sup>.

A reference for the ONTAP REST API can be found [here.](https://library.netapp.com/ecmdocs/ECMLP2856304/html/index.html)<sup>**</sup>.

*You can view all inexpensive fields with the `fields=*` query, and all expensive fields using `fields=**` query

**Since this system is in a lab environment, the practice API does not require SSL Verification.

## Requirements

### What we're looking for

Other than the successful completion of the task, some requirements that we're looking for include:

- Golang (preferred) or Python usage
- Clear, concise and consistent code
- Usage documentation
- Testing of core functionality

### Some nice-to-haves

If time permits, we would also love to see:

- Mocking / DI pattern implementation
- OpenAPI schema definition
- Error handling
- Meaningful logging and comments

### No need to implement

We're mostly interested in your ability to write clean code that can be understood and built on by others, so there's no need to worry about features such as:

- Authentication and authorisation
- Filtering and pagination
- Caching and other optimisation concerns

## Final

When complete, please email your code to the sender for review. The exercise should only take a few hours, however there is no time limit on your submission since we understand life is busy. Feel free to reach out as you need if you have any further questions or clarifications.