%global packname  asciiSetupReader
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Reads Fixed-Width ASCII Data Files (.txt or .dat) that HaveAccompanying Setup Files (.sps or .sas)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-zoo 

%description
Lets you open a fixed-width ASCII file (.txt or .dat) that has an
accompanying setup file (.sps or .sas). These file combinations are
sometimes referred to as .txt+.sps, .txt+.sas, .dat+.sps, or .dat+.sas.
This will only run in a txt-sps or txt-sas pair in which the setup file
contains instructions to open that text file. It will NOT open other text
files, .sav, .sas, or .por data files. Fixed-width ASCII files with setup
files are common in older (pre-2000) government data.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX