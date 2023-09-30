% 111c51502
% CY Fu
% NTUT-UTA AI-EMBA Program
% 2023/09/23

% Generate data set
rng('default')  % Set random number generator to default for reproducibility
category1 = randn(100,2) + [1 1];
category2 = randn(100,2) + [-1 -1];

figure;
plot(category1(:,1), category1(:,2), 'r.', 'MarkerSize', 15);
hold on;
plot(category2(:,1), category2(:,2), 'b.', 'MarkerSize', 15);
xlabel('X');
ylabel('Y');

title({'pr_hw#01B_111c51502' ; 'Training Data Set'}, 'Interpreter', 'none')

% Combine data
allData = [category1; category2];
labels = [ones(size(category1, 1), 1); 2*ones(size(category2, 1), 1)];

% 1-NN classifier
Mdl1 = fitcknn(allData, labels, 'NumNeighbors', 1);

% 15-NN classifier
Mdl15 = fitcknn(allData, labels, 'NumNeighbors', 15);

% Generate a grid
xRange = linspace(-6, 6, 300);
yRange = linspace(-6, 6, 300);
[Zx, Zy] = meshgrid(xRange, yRange);

% Prediction function
Z1 = arrayfun(@(x, y) predict(Mdl1, [x y]), Zx, Zy);
Z15 = arrayfun(@(x, y) predict(Mdl15, [x y]), Zx, Zy);

% Draw decision boundaries
[~, h2] = contour(Zx, Zy, Z1, [1.5, 1.5], 'g', 'LineWidth', 2);
[~, h3] = contour(Zx, Zy, Z15, [1.5, 1.5], 'm', 'LineWidth', 2);
legend('Class-1', 'Class-2', '1-NN Boundary', '15-NN Boundary');
