# Project Charter

## SA National Roads Data Platform
South African National Roads Data Platform

___
## Project Overview
The South African National Roads Data Platform is a data-driven system that integrates, manages, analyses, and simulates publicly available data relating to South Africa's national road network. The platform provides operational insights into road disruptions and their impact on transport operations and corridor performance.

___
## Project Vision
Develop a centralized road data platform that demonstrates how publicly available transport data can be transformed into actionable insights through data engineering, analytics, and simulation.

___
## Problem Statement
South Africa's national roads play a critical role in supporting freight movement, economic activity, and regional connectivity. Disruptions such as road closures, traffic incidents, severe weather, and infrastructure constraints can significantly impact transport efficiency and operating costs.

Publicly available road data is often distributed across multiple sources, which can make it difficult to analyse road performance and evaluate the potential impact of different operational scenarios.

___
## Project Objective
To design and implement a centralized road intelligence platform that integrates publicly available South African national road datasets, provides structured data storage and analytical capabilities, and supports scenario based simulations to improve operational planning and decision making.

___
## Project Scope
### Included (Version 1)

#### Data Management
- Collect publicly available South African national road datasets
- Clean and validate imported data
- Store structured data in a relational SQL database
- Store and manage simulation results

#### Simulation
- Simulate operational scenarios affecting selected national roads
- Model disruptions such as accidents, weather events, and road closures
- Compare scenario outcomes

#### Analytics
- Calculate road and simulation performance indicators
- Generate summary reports
- Identify performance trends

#### Dashboard
- Display road network data
- Visualise simulation results
- Present key performance indicators (KPIs)

#### Documentation
- Project documentation
- Data dictionary
- Assumptions register
- Database design
- Architecture documentation

___
### Not Included (Version 1)
- Machine learning
- Predictive forecasting
- Live traffic data
- Live weather integration
- Cloud deployment
- User authentication
- Advanced optimisation algorithms

___
## Stakeholders

|Stakeholder       |Interest/Responsibility                                                           |
|---               |                                                                               ---|
|Project Sponsor   |Defines project objectives, manages priorities, and approves deliverables         |
|End Users         |Logistics managers, and students who use the platform's analyses and simulations  |
|Data Providers    |Organizations that publish the public national road datasets used by the platform |

___
## Success Criteria

Version 1 will be considered successful when:
- Public national road datasets are successfully imported
- Data is cleaned and validated
- Data is stored in a structured database
- Simulation scenarios can be executed
- Results are stored and analysed
- Dashboard displays meaningful KPIs
- Documentation is complete
- Project is published with a clear README

___
## Project Constraints

- Limited to publicly available South African national road datasets
- Dependent on the quality and availability of external data sources
- Developed using open-source technologies and free development tools
- Version 1 is limited to offline analysis and excludes real-time data integration, predictive analytics, and cloud deployment

___
## Future Enhancements
Potential future versions may include:

- Live SANRAL data integration
- Real-time traffic monitoring
- Additional national roads
- Route optimisation
- Predictive analytics
- Machine learning models
- Multi-user support
- Cloud deployment
