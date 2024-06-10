expArrays = getExpData();

test = expArrays{1};

plot(expArrays{1}{:,2}, expArrays{1}{:,6});
xlabel('temps (s)');
ylabel('amplitude');
title('Channel 1')