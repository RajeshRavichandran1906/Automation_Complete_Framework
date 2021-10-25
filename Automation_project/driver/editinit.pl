#!/usr/local/bin/perl

use Cwd;
#$workspace=getcwd();
$prodid = shift(@ARGV);
$confid = shift(@ARGV);
$relid = shift(@ARGV);
$browser = shift(@ARGV);
$suiteFolder = shift(@ARGV);

$suite=$suiteFolder;
$suite=~ s/.*\// /;
$suite=~ s/^\s*(.*?)\s*$/$1/;
my $Conf = {};
$initFile="${workspace}\\qa\\${suiteFolder}\\"."${suite}.init";
$initFile="${suiteFolder}\\"."${suite}.init";
print "$initFile\n";

my @resp = qx(\\\\bigrepos01\\bigscm\\admin\\bin\\getConf.pl $prodid $confid $relid);
chomp(@resp);
foreach my $resp (@resp) {
    my ($key,$val) = $resp =~ /^(\S+)\s+(.+)$/;
    $Conf->{$key} = $val;
}

if ($browser eq 'ff'){
   $browser='Firefox';
  }elsif($browser eq 'ie'){
    $browser='IE';
   $browser_driver='D:\IEDriverServer.exe';
  }elsif($browser='cr'){
   $browser='Chrome';
   $browser_driver='D:\chromedriver.exe';
  }elsif($browser='sa'){
   $browser='Safari';
  }
  
$nodeid=$Conf->{nodeid};
$httpport=$Conf->{httpport};
$wfcontext=$Conf->{httpport};


open(FILE, $initFile) || die "File not found";
my @lines = <FILE>;
close(FILE);

my @newlines;
foreach(@lines) {
   $_ =~ s/nodeid\s+(.+)/nodeid $nodeid/;
   $_ =~ s/httpport\s+(.+)/httpport $httpport/;
   $_ =~ s/browser\s+(.+)/browser $browser/;
   $_ =~ s/browser_driver\s+(.+)/browser_driver $browser_driver/;
   push(@newlines,$_);
}

open(FILE, ">$initFile") || die "File not found";
print FILE @newlines;
close(FILE);
