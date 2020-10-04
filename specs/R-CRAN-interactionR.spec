%global packname  interactionR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Full Reporting of Interaction Analyses

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-flextable 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-car 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-flextable 

%description
Produces a publication-ready table that includes all effect estimates
necessary for full reporting effect modification and interaction analysis
as recommended by Knol and Vanderweele (2012) [<doi:10.1093/ije/dyr218>].
It also estimates confidence interval for the trio of additive interaction
measures using the delta method (see Hosmer and Lemeshow (1992),
[<doi:10.1097/00001648-199209000-00012>]), variance recovery method (see
Zou (2008), [<doi:10.1093/aje/kwn104>]), or percentile bootstrapping (see
Assmann et al. (1996), [<doi:10.1097/00001648-199605000-00012>]).

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

%files
%{rlibdir}/%{packname}
