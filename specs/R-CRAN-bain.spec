%global packname  bain
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Bayes Factors for Informative Hypotheses

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Computes approximated adjusted fractional Bayes factors for equality,
inequality, and about equality constrained hypotheses. S3 methods are
available for specific types of lm() models, namely ANOVA, ANCOVA, and
multiple regression, and for the t_test(). The statistical underpinnings
are described in Hoijtink, Mulder, van Lissa, and Gu, (2018)
<doi:10.31234/osf.io/v3shc>, Gu, Mulder, and Hoijtink, (2018)
<doi:10.1111/bmsp.12110>, Hoijtink, Gu, and Mulder, (2018)
<doi:10.1111/bmsp.12145>, and Hoijtink, Gu, Mulder, and Rosseel, (2018)
<doi:10.1037/met0000187>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs