F1 SCORE:

It tells how well the model balancing precision and recall.

This prevents a model from looking good just because one metric is high.

the precision or recall alone are not good enough as both should be balanced to maintain high f1 score 


The F1 score prefers balance between precision and recall because it is defined as their harmonic mean:



The harmonic mean is designed to be strongly influenced by the smaller of the two values.



the harmonic mean emphasizes the weaker component, making it impossible to achieve a high F1 unless both precision and recall are high.