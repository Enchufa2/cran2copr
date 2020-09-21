%global packname  TestDimorph
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis Of The Interpopulation Difference In Degree of Sexual Dimorphism Using Summary Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-cutpointr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-utils 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-cutpointr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-truncnorm 
Requires:         R-utils 

%description
Provides two approaches of comparison; the univariate and the multivariate
analysis in two or more populations. Since the main obstacle of performing
systematic comparisons in anthropological studies is the absence of raw
data, the current package offer a solution for this problem by allowing
the use of published summary statistics of metric data (mean, standard
deviation and sex specific sample size) as illustrated by the works of
Greene, D. L. (1989) <doi:10.1002/ajpa.1330790113> and Konigsberg, L. W.
(1991) <doi:10.1002/ajpa.1330840110>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
