%global packname  CornerstoneR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Collection of Scripts for Interface Between 'Cornerstone' and'R'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.9.1
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-vcd 
Requires:         R-CRAN-checkmate >= 1.9.1
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-vcd 

%description
Collection of generic 'R' scripts which enable you to use existing 'R'
routines in 'Cornerstone'. --- The desktop application 'Cornerstone'
(<https://www.camline.com/en/products/cornerstone/cornerstone-core.html>)
is a data analysis software provided by 'camLine' that empowers
engineering teams to find solutions even faster. The engineers incorporate
intensified hands-on statistics into their projects. They benefit from an
intuitive and uniquely designed graphical Workmap concept: you design
experiments (DoE) and explore data, analyze dependencies, and find answers
you can act upon, immediately, interactively, and without any programming.
--- While 'Cornerstone's' interface to the statistical programming
language 'R' has been available since version 6.0, the latest interface
with 'R' is even much more efficient. 'Cornerstone' release 7.1.1 allows
you to integrate user defined 'R' packages directly into the standard
'Cornerstone' GUI. Your engineering team stays in 'Cornerstone's'
graphical working environment and can apply 'R' routines, immediately and
without the need to deal with programming code. --- Learn how to use 'R'
packages in 'Cornerstone' 7.1.1 on 'camLineTV' YouTube channel
(<https://www.youtube.com/watch?v=HEQHwq_laXU>) (available in German).

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/csdata
%doc %{rlibdir}/%{packname}/variablesdialog
%{rlibdir}/%{packname}/INDEX