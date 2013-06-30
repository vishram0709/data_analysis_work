

select B.docid,sum(B.count) from vishal as A,frequency as B where A.docid='q' and A.term=B.term group by B.docid order by sum(B.count) DESC ;
