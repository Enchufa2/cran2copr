#!/usr/bin/env Rscript

source("config.r")
source("common.r")
check_copr()

args <- get_args("Usage: ", script_name(), " [--all | pkg1 ...]")

cran <- available.packages()
copr <- get_copr_list(args)

pkgs <- split(copr, copr %in% cran[,"Package"])
pkgs.del <- pkgs[["FALSE"]]
pkgs.upd <- pkgs[["TRUE"]]
pkgs.upd <- pkgs.upd[need_update(pkgs.upd, cran)]
pkgs.upd <- with_deps(pkgs.upd, cran)
pkgs.upd <- pkgs.upd[need_update(pkgs.upd, cran)]

if (length(pkgs.del))
  system2("./copr-del.r", paste(pkgs.del, collapse=" "))
if (length(pkgs.upd))
  system2("./copr-add.r", paste(pkgs.upd, collapse=" "))
