
%{
This code plots the refractive index of all material data
%}

%% Load material Files
[File, FileName, PathName] = get_file;

%% Form materials Struct
materials = struct('name',[],'n',[],'k',[],'lda',[]);
for idx = 1:length(File)
    load(File{idx})
    materials(idx).name = FileName{idx}; % erase(FileName{idx},'.mat');
    materials(idx).n = n;
    materials(idx).k = k;
    materials(idx).lda = lda;
    clearvars n k lda
end


%% Make plots

figure, 
for idx = 1:length(File)
    plot(materials(idx).lda, materials(idx).n)
    hold on 
end










