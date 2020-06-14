%global packname  parallelMap
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          2%{?dist}
Summary:          Unified Interface to Parallelization Back-Ends

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.8.0
BuildRequires:    R-CRAN-BBmisc >= 1.8
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate >= 1.8.0
Requires:         R-CRAN-BBmisc >= 1.8
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Unified parallelization framework for multiple back-end, designed for
internal package and interactive usage.  The main operation is parallel
mapping over lists.  Supports 'local', 'multicore', 'mpi' and 'BatchJobs'
mode.  Allows tagging of the parallel operation with a level name that can
be later selected by the user to switch on parallel execution for exactly
this operation.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/test_source_file.R
%{rlibdir}/%{packname}/INDEX
