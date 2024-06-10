expArrays = getExpData();

test = expArrays{1};

plot(expArrays{1}{:,2}, expArrays{1}{:,6});
xlabel('time (seconds)');
ylabel('Hb');
title('channel 1')

hold on

plot(expArrays{1}{:,2}, expArrays{1}{:,7})
legend("oxygenated blood", "desoxygenated blood")

hold off