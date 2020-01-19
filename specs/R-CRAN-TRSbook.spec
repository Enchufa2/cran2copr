%global packname  TRSbook
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Functions and Datasets to Accompany the Book "The R Software:Fundamentals of Programming and Statistical Analysis"

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-IndependenceTests 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-IndependenceTests 

%description
Functions and datasets for the reader of the book "The R Software:
Fundamentals of Programming and Statistical Analysis".

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/cor.test.2.sample.R
%doc %{rlibdir}/%{packname}/HISTORY
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs