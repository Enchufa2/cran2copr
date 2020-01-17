%global packname  GGIR
%global packver   1.11-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.0
Release:          1%{?dist}
Summary:          Raw Accelerometer Data Analysis

License:          LGPL (>= 2.0, < 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-GENEAread 
BuildRequires:    R-CRAN-tuneR 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-GENEAread 
Requires:         R-CRAN-tuneR 

%description
A tool to process and analyse data collected with wearable raw
acceleration sensors as described in van Hees and colleagues (2014) <doi:
10.1152/japplphysiol.00421.2014> and (2015) <doi:
10.1371/journal.pone.0142533>. The package has been developed and tested
for binary data from 'GENEActiv' <https://www.activinsights.com/> and
GENEA devices (not for sale), .csv-export data from 'Actigraph'
<http://actigraphcorp.com> devices, and .cwa and .wav-format data from
'Axivity' <https://axivity.com/product/ax3>. These devices are currently
widely used in research on human daily physical activity. Further, the
package can handle accelerometer data file from any other sensor brand
providing that the data is stored in csv format and has either no header
or a two column header.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/testfiles
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
