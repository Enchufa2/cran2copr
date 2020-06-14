%global packname  rdmulti
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          2%{?dist}
Summary:          Analysis of RD Designs with Multiple Cutoffs or Scores

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rdrobust 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rdrobust 

%description
The regression discontinuity (RD) design is a popular quasi-experimental
design for causal inference and policy evaluation. The 'rdmulti' package
provides tools to analyze RD designs with multiple cutoffs or scores:
rdmc() estimates pooled and cutoff specific effects for multi-cutoff
designs, rdmcplot() draws RD plots for multi-cutoff designs and rdms()
estimates effects in cumulative cutoffs or multi-score designs. See
Cattaneo, Titiunik and Vazquez-Bare (2020)
<https://sites.google.com/site/rdpackages/rdmulti/Cattaneo-Titiunik-VazquezBare_2020_Stata.pdf>
for further methodological details.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
