%global packname  st
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Shrinkage t Statistic and Correlation-Adjusted t-Score

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.9
BuildRequires:    R-CRAN-sda >= 1.3.7
BuildRequires:    R-CRAN-fdrtool >= 1.2.15
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-corpcor >= 1.6.9
Requires:         R-CRAN-sda >= 1.3.7
Requires:         R-CRAN-fdrtool >= 1.2.15
Requires:         R-graphics 
Requires:         R-stats 

%description
Implements the "shrinkage t" statistic introduced in Opgen-Rhein and
Strimmer (2007) <DOI:10.2202/1544-6115.1252> and a shrinkage estimate of
the "correlation-adjusted t-score" (CAT score) described in Zuber and
Strimmer (2009) <DOI:10.1093/bioinformatics/btp460>. It also offers a
convenient interface to a number of other regularized t-statistics
commonly employed in high-dimensional case-control studies.

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
