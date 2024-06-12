function displayData(startValue, endValue, data)

figure('Name',['Visualisation of channels ', num2str(startValue), ' - ', num2str(endValue)], 'Numbertitle','off');

for k=0+startValue : endValue
    subplot(round((endValue-startValue)/2),2,k-(startValue-1));

    plot(data{1}{:,2}, data{1}{:,6+3*(k-1)});
    xlabel('time (seconds)');
    ylabel('Hb');
    title(['channel n°', num2str(k)])
    hold on
    
    plot(data{1}{:,2}, data{1}{:,7+3*(k-1)})
    legend("oxygenated blood", "desoxygenated blood")
    hold off
end

