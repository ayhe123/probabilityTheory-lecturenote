# probabilityTheory-lecturenote
何书元《概率引论》笔记及课后习题答案

这是我在B站看何书元老师的《概率论》课程时作的笔记以及《概率引论》一部分课后习题的答案，供大家参考，也请各位大佬帮忙修改。

下面的 “教材” 指何书元老师的《概率引论》，“课程”指何书元老师的《概率论》课程。

## 课程和教材的简要介绍

课程是何书元老师在首都师范大学录的，讲的是初等概率论，个人感觉难度不大。何书元老师讲课风趣幽默，经常将概率论与日常生活联系起来，总的来说还是很值得看的。

教材是与课程配套的，很薄的一本书，我大概花了两个月时间就看完了视频，把教材里会写的题都写了一遍。

## 仿真

对于一些比较难理解的题目和定理，我也用 `Python` 写了仿真，放在 `simulation` 文件夹下。目前只做了 4 个仿真，如果有需要的话还可以接着做。

仿真需要安装 `numpy` 和 `matplotlib`：

```bash
pip3 install numpy
pip3 install matplotlib
```

之后就应该可以直接运行仿真。

## 使用方法

由于只有一个 $\LaTeX$ 文件，所以我就不像[代数学笔记](https://github.com/ayhe123/algebra-lecturenote)那样打包编译好的文档了，仓库里的 `lecturenote_bg.pdf` 和 `lecturenote.pdf` 是我编译好的文档，分别是有背景颜色的和没有背景颜色的。

这个笔记使用 [ElegantNote 模板](https://github.com/ElegantLaTeX/ElegantNote)，我对 ElegantNote 进行了一些修改，主要是加入了一些 `mdframed` 定理环境，[源码地址](https://github.com/ayhe123/ElegantNote)

想要自己编译的话，在 Linux 或者 MacOS 下执行：

```bash
git clone https://github.com/ayhe123/probabilityTheory-lecturenote.git
git clone https://github.com/ayhe123/ElegantNote.git
cp ElegantNote/elegantnote.cls algebra-lecturenote
```

然后用 `xelatex` 编译即可。

也可以使用原版 ElegantNote，方法在[代数学笔记](https://github.com/ayhe123/algebra-lecturenote)那里有介绍。

## 许可证

本笔记以及仿真采用 CC-BY-4.0 许可证, 更多信息见 https://creativecommons.org/licenses/by/4.0

笔记的页脚中的 [图片](license.eps) 来自 https://creativecommons.org/about/downloads/
