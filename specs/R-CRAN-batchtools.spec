%global packname  batchtools
%global packver   0.9.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.13
Release:          2%{?dist}
Summary:          Tools for Computation on Batch Systems

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-withr >= 2.0.0
BuildRequires:    R-CRAN-checkmate >= 1.8.5
BuildRequires:    R-CRAN-fs >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.11.2
BuildRequires:    R-CRAN-backports >= 1.1.2
BuildRequires:    R-CRAN-progress >= 1.1.1
BuildRequires:    R-CRAN-base64url >= 1.1
BuildRequires:    R-CRAN-digest >= 0.6.9
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
Requires:         R-CRAN-withr >= 2.0.0
Requires:         R-CRAN-checkmate >= 1.8.5
Requires:         R-CRAN-fs >= 1.2.0
Requires:         R-CRAN-data.table >= 1.11.2
Requires:         R-CRAN-backports >= 1.1.2
Requires:         R-CRAN-progress >= 1.1.1
Requires:         R-CRAN-base64url >= 1.1
Requires:         R-CRAN-digest >= 0.6.9
Requires:         R-CRAN-brew 
Requires:         R-parallel 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rappdirs 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-utils 

%description
As a successor of the packages 'BatchJobs' and 'BatchExperiments', this
package provides a parallel implementation of the Map function for high
performance computing systems managed by schedulers 'IBM Spectrum LSF'
(<https://www.ibm.com/us-en/marketplace/hpc-workload-management>),
'OpenLava' (<http://www.openlava.org/>), 'Univa Grid Engine'/'Oracle Grid
Engine' (<http://www.univa.com/>), 'Slurm' (<http://slurm.schedmd.com/>),
'TORQUE/PBS'
(<https://adaptivecomputing.com/cherry-services/torque-resource-manager/>),
or 'Docker Swarm' (<https://docs.docker.com/swarm/>). A multicore and
socket mode allow the parallelization on a local machines, and multiple
machines can be hooked up via SSH to create a makeshift cluster. Moreover,
the package provides an abstraction mechanism to define large-scale
computer experiments in a well-organized and reproducible way.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/bin
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
