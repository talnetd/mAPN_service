# mAPNservice
This API service will provide a facility for frontend BMS to call when they want to talk to network devices such as routers and OLT panels.

## TOPOLOGY
![BMS TOPOLOGY](assets/topology.png?raw=true "BMS TOPOLOGY")
*Overall architecture of the stack*

## FLOWCHARTS
![CRM-TO-BMS-TO-RADIUS](assets/flow_chart_crm2bms2radius.png?raw=true "BMS FLOWCHART")
*Flowchart to describe how we build resources starting from location to radius packages*

## Getting Started

To get started developing/testing this software service, you may need the
following installed in your executable path aka $PATH.

1. python3
2. pip3
3. pyenv or equivalent

> NOTE: For detail installation, please check **INSTALL.md**.

### Prerequisites

We are using pip dependencies we will use requirements.txt as lock file. Run
the follow command.


```
cd ~/your_project_path
pip3 install -r requirements.txt
```

## Running the services

There is a script under the project root for you too run the service. Just
simply chmod +x the script if we haven't done so yet.

```
./dev_server.sh
```

## Other Service
### TALNET's local lab

* MIKROTIK: 192.168.100.114
* RADIUS: 192.168.100.120
* NASUSER: radius
* NAS_SECRET: nerdb0rn

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **TALNET** - *Initial work* - [Github](https://github.com/talnetd)
* **LMK** - *CoreDev* - [Github](https://github.com/laminko)
