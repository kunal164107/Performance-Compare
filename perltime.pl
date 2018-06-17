#!/usr/bin/perl 
use strict;
use warnings;
my @names = ("10MB.txt","20MB.txt","30MB.txt","40MB.txt","50MB.txt");
my @perltime12;

my $resultfile ="ptemp.csv";
open( my $fh, ">>", $resultfile )  or die $!;

for(my $i=0;$i<5;$i=$i+1){
my $start123 = time();
my $defaultfile = $names[$i];
my $mainfile ="copyperl.txt";
open( my $default_fh, "<", $defaultfile ) or die $!;
open( my $main_fh,    ">", $mainfile ) or die $!;
while ( my $line = <$default_fh> ) {
    print {$main_fh} $line;
}
close $default_fh;
close $main_fh;

my $end123 = time();
$perltime12[$i]= $end123-$start123;
print {$fh} $perltime12[$i];
print {$fh} ",";
}
print {$fh} "\n";
close $fh;
# print "@perltime12\n";
