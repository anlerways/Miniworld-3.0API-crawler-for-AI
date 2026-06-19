# 《迷你世界》UGC 3.0 枚举参考手册
> GitHub开源仓库: https://github.com/anlerways/Miniworld-3.0API-crawler-for-AI
> 本文档由爬虫自动生成，数据来源：https://dev-wiki.mini1.cn/ugc-wiki/

## Ability
- `Attack` = 普通攻击
- `Break` = 破坏方块
- `CanBePickup` = 可被举起
- `CanUseItemWhenBePickup` = 被举起时可否使用道具
- `Cube` = 方块能力总开关
- `Drop` = 丢弃道具
- `EnableBeattacked` = 可受伤
- `EnableBekilled` = 可被杀死
- `EnableDeathdropitem` = 杀死有掉落物
- `EnableInputRotate` = 玩家输入旋转(玩家生效)
- `EnableRotatingCamera` = 可旋转摄像机
- `EnableSwitchShortcut` = 可切换快捷栏
- `Flying` = 飞行
- `Interaction` = 交互方块
- `Item` = 道具能力总开关
- `Jumping` = 跳跃
- `Movement` = 移动能力总开关
- `Pick` = 拾取道具
- `Place` = 摆放方块
- `Sneaking` = 潜行
- `Sprinting` = 疾跑
- `Swimming` = 游泳
- `Use` = 使用道具
- `Walking` = 行走

## AbsoluteCampType
- `Enemy` = 中立敌对
- `Noteam` = 无队伍
- `Passive` = 中立被动
- `Team1` = 队伍1
- `Team2` = 队伍2
- `Team3` = 队伍3
- `Team4` = 队伍4
- `Team5` = 队伍5
- `Team6` = 队伍6
- `TeamNpc1` = 绝对阵营-npc队伍1
- `TeamNpc2` = 绝对阵营-npc队伍2
- `TeamNpc3` = 绝对阵营-npc队伍3

## AnimMode
- `Default` = 表格默认值播放
- `Loop` = 循环播放
- `Once` = 播放一次
- `OnceStop` = 播放一次完毕，停在末尾

## AreaCloneType
- `ExcludeAir` = 复制(不含空气)
- `ExcludeAirAndMove` = 移动(不含空气)
- `IncludeAir` = 复制(含空气)
- `IncludeAirAndMove` = 移动(含空气)

## AreaFillType
- `Delete` = 删除
- `Destroy` = 摧毁

## AvtPart
- `BackOrnament` = 背装饰
- `BgEffect` = 背景特效
- `Body` = 身体
- `EquipBreast` = 装备胸部
- `EquipCustom1` = 装备扩展1
- `EquipCustom2` = 装备扩展2
- `EquipCustom3` = 装备扩展3
- `EquipHead` = 装备头部
- `EquipLegging` = 装备腿部
- `EquipPifeng` = 装备披风
- `EquipShoe` = 装备鞋子
- `EquipWeapon` = 装备武器
- `Face` = 脸
- `FaceEffect` = 脸特效
- `FaceOrnament` = 脸装饰
- `Footprint` = 脚印
- `HandEffect` = 手特效
- `HandOrnament` = 手装饰
- `Head` = 头部
- `HeadEffect` = 头部特效
- `Jacket` = 夹克
- `Max` = 最大值
- `RightHand` = 右手特效
- `RightShoe` = 右脚特效
- `Shoe` = 鞋子
- `Skin` = 皮肤
- `TrailingEffect` = 拖尾特效
- `Trousers` = 裤子
- `WholeBodyEffect` = 全身特效
- `WingEffect` = 翅膀特效

## BackpackBeginIndex
- `Equip` = 装备栏
- `ExtBackpack` = 扩展背包
- `Inventory` = 存储栏
- `Shortcut` = 快捷栏

## BackpackType
- `Equip` = 装备栏
- `Extend` = 扩展背包
- `Inventory` = 存储栏
- `Shortcut` = 快捷栏

## BeaconClampType
- `Circle` = 圆形限制
- `None` = 无限制
- `Rectangle` = 矩形限制

## BeaconMapType
- `Object` = 对象
- `Position` = 位置

## BiomeType
- `AirShipFleet` = 铁穹舰队
- `AirShipPlain` = 铁穹平原
- `Airland` = 迷拉星空岛
- `AirlandAir` = 迷拉星空岛空中
- `AirlandGround` = 迷拉星空岛地上
- `AirlandShine` = 迷拉星粉蝶花空岛
- `Basin` = 迷拉星盆地
- `BasinBamboo` = 迷拉星竹林盆地
- `BasinEdge` = 迷拉星盆地边缘
- `BasinLake` = 迷拉星盆地湖泊
- `BasinPeach` = 迷拉星桃树盆地
- `BasinRice` = 迷拉星盆地稻田
- `Beach` = 迷拉星沙滩
- `Canyon` = 迷拉星峡谷
- `CanyonEage` = 迷拉星峡谷边缘
- `City` = 迷拉星末日城镇
- `Cliff` = 迷拉星峭壁
- `CliffEdge` = 迷拉星峭壁边缘
- `CliffGinkgo` = 迷拉星峭壁银杏林
- `CliffMaple` = 迷拉星峭壁枫叶林
- `CliffPlum` = 迷拉星三角梅峭壁
- `ConiferousForest` = 迷拉星针叶林
- `ConiferousForestHills` = 迷拉星针叶林山丘
- `ConiferousForestLake` = 迷拉星针叶林湖泊
- `DeepSea` = 迷拉星深海
- `Desert` = 迷拉星沙漠
- `DesertHills` = 迷拉星沙漠山丘
- `DesertLake` = 迷拉星沙漠湖泊
- `DesertOasis` = 迷拉星沙漠绿洲
- `DesertPopulusEuphratica` = 迷拉星沙漠胡杨林
- `Earthcore` = 烈焰星熔岩之地
- `EyedStarAirlands` = 萌眼星空岛
- `EyedStarAirlandsEdge` = 萌眼星空岛边缘
- `EyedStarAirlandsSub1` = 萌眼星子空岛1
- `EyedStarAirlandsSub2` = 萌眼星子空岛2
- `EyedStarAirlandsSub3` = 萌眼星子空岛3
- `EyedStarAirlandsSub4` = 萌眼星子空岛4
- `EyedStarGround` = 萌眼星地表
- `EyedStarGroundHills` = 萌眼星山丘
- `EyedStarGroundHills2` = 萌眼星山丘2
- `EyedStarGroundMountain` = 萌眼星高山
- `EyedStarGroundPlain` = 萌眼星祭坛平原
- `Forest` = 迷拉星森林
- `ForestChrysanth` = 迷拉星森林菊花花海
- `ForestFoxtail` = 迷拉星森林狗尾草海
- `ForestHills` = 迷拉星森林山丘
- `ForestLake` = 迷拉星森林湖泊
- `ForestLavender` = 迷拉星森林薰衣草花海
- `FrozenRiver` = 迷拉星冻河
- `FrozenSea` = 迷拉星冻洋
- `GrassLand` = 迷拉星草原
- `GrassLandArid` = 迷拉星干旱草原
- `GrassLandDandelion` = 迷拉星草原蒲公英花海
- `GrassLandRapeseed` = 迷拉星草原油菜花海
- `IceMountains` = 迷拉星冰山
- `IceSheet` = 迷拉星冰原
- `IceSheetConiferousForest` = 迷拉星覆雪针叶林
- `IceSheetFrizebLake` = 迷拉星雪山冻湖
- `IceSheetHighestPeak` = 迷拉星雪山主峰
- `IceSheetMountain` = 迷拉星雪山山脉
- `IceSheetMountainSide` = 迷拉星雪山中部
- `IceSheetPeakPlain` = 迷拉星雪山底部
- `IceSheetSecondMountainSide` = 迷拉星雪山副峰中部
- `IceSheetSecondPeak` = 迷拉星雪山副峰
- `IslandLandDesert` = 迷拉星荒岛岛心
- `IslandLandRedsoil` = 迷拉星红土岛心
- `IslandLandReef` = 迷拉星珊瑚岛岛心
- `IslandLandTulip` = 迷拉星郁金香岛心
- `IslandShoreDesert` = 迷拉星荒岛海岸
- `IslandShoreRedsoil` = 迷拉星红土岛海岸
- `IslandShoreReef` = 迷拉星珊瑚岛海岸
- `IslandShoreTulip` = 迷拉星郁金香海岸
- `Jungle` = 迷拉星丛林
- `JungleBlueJacaranda` = 迷拉星丛林蓝花楹树林
- `JungleHills` = 迷拉星丛林山丘
- `PlainsLake` = 迷拉星草原湖泊
- `RainForest` = 迷拉星雨林
- `RainForestLake` = 迷拉星雨林湖泊
- `RedSoil` = 迷拉星红土
- `RedSoilShore` = 迷拉星红土海岸
- `River` = 迷拉星河流
- `Sea` = 迷拉星浅海
- `Swamp` = 迷拉星沼泽
- `SwampRiverSide` = 迷拉星沼泽河畔
- `Volcano` = 迷拉星火山主峰
- `VolcanoCore` = 迷拉星火山口
- `VolcanoMountain` = 迷拉星火山山脉
- `VolcanoPlain` = 迷拉星火山平原
- `VolcanoRiver` = 迷拉星火山岩浆河

## BlockAttr
- `BurningProbability` = 燃烧几率
- `BurningSpeed` = 燃烧速度
- `ExplodeResistance` = 爆炸抗性
- `Glissade` = 滑行惯性
- `Hardness` = 硬度
- `Lightness` = 亮度

## BlockLimits
- `BepushedDropItem` = 被推动掉落
- `EnableBeoperated` = 可操作
- `EnableBepushed` = 可被推动
- `EnableDestroyed` = 可破坏
- `EnableDropItem` = 可掉落道具

## BlockStatus
- `Active` = 活跃(被激活)
- `Inactive` = 不活跃(未被激活)

## CameraEditState
- `Edit` = 编辑
- `Null` = 空
- `Test` = 测试

## CameraModel
- `Autoindent` = 阻挡后自动缩进
- `MoveFollow` = 跟随角色移动
- `RelativeRotate` = 相对人物旋转
- `RoleTranslucent` = 角色半透
- `RotateFollow` = 跟随角色旋转

## CameraRotate
- `AllDir` = 全方向
- `NoTurn` = 无法转动
- `OnlyPitch` = 仅上下
- `OnlyYaw` = 仅左右

## CmpProPermission
- `Private` = 私有
- `Public` = 公开
- `Read` = 只读

## CmpUIPermission
- `Hide` = 隐藏
- `Show` = 显示

## CreatureAttr
- `Atk` = 攻击力
- `AtkMagic` = 元素攻击
- `AtkMelee` = 近战攻击
- `AtkPhysical` = 物理攻击
- `AtkRemote` = 远程攻击
- `AttackDis` = 攻击距离
- `BodyLerpSpeed` = 转身速度
- `CurHp` = 当前生命值
- `CurHunger` = 当前饥饿值
- `CurOxygen` = 当前氧气值
- `DefChaos` = 混乱防御
- `DefMagic` = 元素防御
- `DefMelee` = 近战防御
- `DefPhysical` = 物理防御
- `DefRemote` = 远程防御
- `Dimension` = 模型大小
- `Dodge` = 闪避率
- `EnableAttack` = 可攻击
- `EnableBeattacked` = 可被攻击
- `EnableBekilled` = 可被杀死
- `EnableDeathdropitem` = 死亡掉落
- `EnableMove` = 可移动
- `EnablePickup` = 可拾取道具
- `ExtraHp` = 临时生命值
- `FlySpeed` = 飞行速度
- `HpRecover` = 生命恢复
- `JumpPower` = 跳跃力
- `Level` = 等级
- `MaxHp` = 最大生命值
- `MaxHunger` = 最大饥饿值
- `PackSize` = 背包空间
- `SwinSpeed` = 游泳速度
- `Toughness` = 韧性值
- `ViewDis` = 视野范围
- `ViewDistance` = 视野距离
- `WalkSpeed` = 移动速度

## CreatureMotion
- `AtkMelee` = 近战攻击
- `AtkRemote` = 远程攻击
- `Beattracted` = 被吸引
- `Copulation` = 交配
- `Follow` = 跟随
- `Idle` = 空闲
- `RunAway` = 逃跑
- `SelfBomb` = 自爆
- `Standby` = 待机
- `Stroll` = 闲逛
- `Swim` = 游泳

## CustomModType
- `Actor` = 实体
- `Biome` = 地形插件
- `Block` = 方块插件 预制
- `Furnace` = 熔炼插件
- `Item` = 道具插件
- `Monster` = 生物插件
- `Recipe` = 配方插件
- `Rule` = 世界规则
- `Status` = 状态插件
- `UI` = UI

## DeviceType
- `Android` = 安卓
- `IOS` = 苹果
- `Other` = 其他
- `PC` = PC端

## DropMode
- `ChangePlayMode` = 掉落物对象转玩法创建
- `DefeatMob` = 生物被击败掉落
- `DestroyBlock` = 方块被破坏掉落
- `DestroyBox` = 箱子被破坏掉落
- `DiscardItem` = 丢弃道具
- `SpawnItem` = 触发器创建

## Easing
- `BackIn` = 回退曲线1渐入
- `BackInOut` = 回退曲线3进出
- `BackOut` = 回退曲线2渐出
- `BounceIn` = 弹跳曲线1渐入
- `BounceInOut` = 弹跳曲线1进出
- `BounceOut` = 弹跳曲线1渐出
- `CircIn` = 圆曲线1渐入
- `CircInOut` = 圆曲线3进出
- `CircOut` = 圆曲线2渐出
- `ElasticIn` = 弹簧曲线1渐入
- `ElasticInOut` = 弹簧曲线3进出
- `ElasticOut` = 弹簧曲线2渐出
- `ExpoIn` = 指数曲线1渐入
- `ExpoInOut` = 指数曲线3进出
- `ExpoOut` = 指数曲线2渐出
- `Linear` = 直线变换
- `None` = 无动画
- `QuadIn` = 平方曲线1渐入
- `QuadInOut` = 平方曲线3进出
- `QuadOut` = 平方曲线2渐出

## ElementAttr
- `Angle` = 角度
- `Color` = 颜色
- `GlobalPos` = 绝对位置
- `Name` = 名称
- `Position` = 位置
- `ScrollPosition` = 滚动容器位置
- `Size` = 尺寸
- `Text` = 文本
- `Transparency` = 透明度
- `Visibility` = 显示/隐藏状态

## ElementType
- `Button` = 按钮
- `InputText` = 输入框
- `Loader3D` = 3d装载器
- `SlidingContainer` = 滑动容器
- `Text` = 文本
- `Texture` = 图片

## EquipSlotType
- `Breast` = 身体
- `Custom1` = 自定义装备位1
- `Custom2` = 自定义装备位2
- `Custom3` = 自定义装备位3
- `Head` = 头
- `Legging` = 腿
- `MaxSlots` = 最大装备栏(用于判断有效性)
- `Pifeng` = 披风
- `Shoe` = 脚
- `Weapon` = 武器

## ErrorCode
- `FAILED` = 失败
- `KV_OP_CD_LMT` = 表设置CD超限
- `KV_OP_INVALID_VAL` = 获取key类型不匹配
- `KV_OP_NO_VAL` = 获取key不存在
- `KV_OP_QPM_LMT` = 表设置QPS/QPM超限
- `KV_UPDATE_GET` = 表安全更新拉取的返回码
- `KV_UPDATE_SET` = 表安全更新设置的返回码
- `OK` = 成功

## EventDate
- `Day` = 日
- `Dayofweek` = 星期几
- `Hour` = 时
- `Minute` = 分
- `Month` = 月
- `Second` = 秒
- `Timestamp` = 时间戳
- `Year` = 年

## FaceDir
- `NegX` = x反方向, 西
- `NegY` = y反方向, 下
- `NegZ` = z反方向, 南
- `None` = 未指定
- `PosX` = x正方向, 东
- `PosY` = y正方向, 上
- `PosZ` = z正方向, 北

## FaceType
- `Pitch` = 面仰角
- `Yaw` = 面朝方向

## GameSetting
- `AutoJump` = 自动跳跃
- `CameraShake` = 镜头晃动
- `FixedMap` = 固定小地图
- `ScopeMode` = 准星模式

## GraphicsType
- `ArrowActor` = 箭头 指向生物
- `ArrowPos` = 箭头 指向位置
- `Brush` = 笔刷
- `Hornbook` = 文字板
- `Image` = 图片
- `LineActor` = 线 指向生物
- `LinePos` = 线 指向位置
- `NavPathPos` = 寻路引导线 指向位置
- `Progress` = 进度条
- `SurfaceActor` = 面 指向生物
- `SurfacePos` = 面 指向界面
- `Suspendbook` = 漂浮文字

## GridAttr
- `Durable` = 耐久度
- `ItemNum` = 道具数量
- `Toughness` = 韧性

## GroupWeatherType
- `Bad` = 恶劣天气
- `Blizzard` = 暴风雪
- `Rain` = 雨天
- `Sandduststorm` = 沙尘暴
- `Shine` = 晴天
- `ShineAndRain` = 晴雨交替
- `Snow` = 雪天
- `Tempest` = 暴风雨
- `Thunder` = 雷暴

## GunAction
- `Aim` = 瞄准待机
- `AimFire` = 瞄准开火
- `AimLoad` = 瞄准手动上膛
- `Equip` = 举枪
- `Fire` = 腰射开火
- `Idle` = 腰射待机
- `Inspect` = 检视
- `Load` = 腰射手动上膛
- `Reload` = 腰射换弹
- `ReloadEmpty` = 腰射空仓换弹
- `Run` = 持枪冲刺

## GunActionBan
- `Aim` = 瞄准待机
- `AimFire` = 瞄准开火
- `AimLoad` = 瞄准手动上膛
- `Equip` = 举枪
- `Fire` = 腰射开火
- `Inspect` = 检视
- `Load` = 腰射手动上膛
- `Reload` = 腰射换弹
- `ReloadEmpty` = 腰射空仓换弹
- `Run` = 持枪冲刺

## GunAttr
- `AdsMoveSpeedBonus` = 瞄准移动速度倍率
- `AdsOffsetX` = 瞄准偏移值
- `AdsOffsetY` = 瞄准偏移值
- `AdsOffsetZ` = 瞄准偏移值
- `AdsSpreadMax` = 瞄准散布最大值
- `AdsSpreadMin` = 瞄准散布最小值
- `AdsSpreadStep` = 瞄准散布步长
- `AdsSpreadType` = 瞄准散布类型
- `AdsSwitchTime` = 瞄准时间
- `AdsSwitchTimeBonus` = 瞄准时间倍率
- `AdsXFunction` = 瞄准镜准星功能
- `AdsXScale` = 瞄准镜准星底图缩放值
- `BaseDamage` = 基础伤害
- `BaseDamageBonus` = 基础伤害倍率
- `BodyDamage` = 躯干倍率
- `BulletConsume` = 消耗子弹数
- `BulletId` = 子弹ID（仅获取预制属性）
- `BulletShrapnel` = 弹片数量
- `ControlValue` = 操控速度（仅取值）
- `DamageType` = 伤害类型
- `DecayFinish` = 衰减结束距离
- `DecayLiquid` = 液体衰减系数
- `DecayMin` = 衰减最小值
- `DecayStart` = 衰减起始距离
- `EquipTime` = 切换枪械行为时间
- `FireType` = 开火类型
- `GunLevel` = 枪械等级 历史遗留的字段，对于游戏本体只用于显示角标
- `HeadDamage` = 头部倍率
- `HipAccValue` = 腰射射击精度（仅取值）
- `HipMoveSpeedBonus` = 腰射移动速度倍率
- `HipSpreadMax` = 腰射散布最大值
- `HipSpreadMin` = 腰射散布最小值
- `HipSpreadStep` = 腰射散布步长
- `HipSpreadType` = 腰射散布类型
- `HittedCameraAngle` = 被击中抬头反馈
- `JumpSpreadBonus` = 跳跃散布倍率
- `MaxAmmo` = 弹容量
- `MoveSpreadBonus` = 移动散布倍率
- `Penetration` = 穿透率
- `Range` = 射程
- `RangeBonus` = 射程倍率
- `RecoilBonus` = 后坐力倍率
- `RecoilPitchBonus` = 垂直后坐力倍率
- `RecoilValue` = 后坐力控制（仅取值）
- `RecoilYawBonus` = 水平后坐力倍率
- `ReloadPhase2Time` = 换弹行为时间
- `ReloadPhase2TimeEmpty` = 空仓换弹行为时间
- `ReloadTimeBonus` = 换弹时间倍率
- `RepelDistance` = 击退距离
- `Rpm` = 射速(每分钟子弹数)
- `RpmBonus` = 射速倍率
- `RunSpreadBonus` = 疾跑散布倍率
- `ScopeMagnification` = 瞄准倍率
- `ScopeXPic` = 瞄准镜准星贴图
- `ShiftMoveSpreadBonus` = 潜行移动散布倍率
- `ShiftSpreadBonus` = 潜行散布倍率
- `SpreadAdsBonus` = 瞄准散布倍率
- `SpreadBonus` = 散布倍率
- `SpreadBonusResetSpeed` = 重置速度
- `SpreadHipBonus` = 腰射散布倍率
- `SpreadResetSpeed` = 重置速度
- `SpreadStepSpeed` = 每发增加速度
- `TouReduce` = 削刃值

## GunDamageType
- `Fire` = 燃烧伤害
- `Ice` = 冰冻伤害
- `Physics` = 物理伤害
- `Poison` = 毒素伤害

## GunFireType
- `Auto` = 全自动
- `Manual` = 手动
- `SemiAuto` = 半自动

## GunSpreadType
- `Circle` = 圆
- `NoRightDown` = 无右下
- `RightUp` = 右上

## GunState
- `Entry` = 进入
- `Exit` = 离开

## HorizontalOffset
- `Centered` = 居中
- `Left` = 居左
- `Right` = 居右

## HurtType
- `All` = 所有伤害（只设置免疫伤害接口有效）
- `Antiinjury` = 反伤 attack_antiinjury
- `Anvil` = 被砸中伤害 attack_anvil
- `Asphyxia` = 窒息伤害 attack_wall
- `Bomb` = 爆炸伤害 attack_explode
- `Burning` = 燃烧伤害 attack_fire
- `Cactus` = 仙人掌伤害 attack_cactus
- `Drown` = 溺水伤害 attack_drown
- `Fall` = 跌落伤害 attack_falling
- `Fixed` = 固定伤害 attack_fixed
- `Flash` = 电元素伤害 attack_flash
- `Ice` = 冰元素伤害 attack_flash
- `Laser` = 被激光伤害 attack_block_laser
- `Melee` = 近战伤害 attack_punch
- `Remote` = 远程伤害 attack_range
- `Suffocate` = 水下生物在空气中窒息伤害 attack_suffocate
- `Sun` = 日晒 attack_sun
- `Toxin` = 毒素伤害 attack_poison
- `Wither` = 凋零伤害 attack_wither

## InnerPopUpview
- `AnimView` = 动作列表界面
- `BackPackEra` = 背包科技界面
- `BackPackRole` = 背包角色界面
- `BackPackTask` = 背包任务界面
- `BuffStatus` = 状态界面
- `CollectMaps` = 收藏地图界面
- `EvaluateMaps` = 评价地图界面
- `InviteFriend` = 邀请好友界面
- `ItemProcessing` = 道具加工界面
- `ItemTips` = 道具提示界面
- `MiniMap` = 小地图界面
- `MiniShop` = 官方商城界面
- `Specialty` = 特长界面
- `StorageBox` = 储物箱界面

## ItemAbility
- `Drop` = 道具不可掉落
- `Throw` = 道具不可丢弃

## ItemAttr
- `Attack` = 攻击力
- `Duration` = 耐久度
- `ExplodeDefense` = 爆炸防御
- `FireDefense` = 燃烧防御
- `FireInterval` = 射击间隔
- `ItemType` = 道具类型
- `LongDefense` = 远程防御
- `Magazines` = 弹夹量
- `PoisonDefense` = 毒素防御
- `Quality` = 品质
- `ShortDefense` = 近战防御
- `Stackmax` = 叠加数
- `WitherDefense` = 混乱防御

## KeyCode
- `A` = 按键A
- `B` = 按键B
- `C` = 按键C
- `D` = 按键D
- `E` = 按键E
- `F` = 按键F
- `G` = 按键G
- `H` = 按键H
- `I` = 按键I
- `J` = 按键J
- `K` = 按键K
- `L` = 按键L
- `M` = 按键M
- `N` = 按键N
- `Number0` = 按键0
- `Number1` = 按键1
- `Number2` = 按键2
- `Number3` = 按键3
- `Number4` = 按键4
- `Number5` = 按键5
- `Number6` = 按键6
- `Number7` = 按键7
- `Number8` = 按键8
- `Number9` = 按键9
- `O` = 按键O
- `P` = 按键P
- `Q` = 按键Q
- `R` = 按键R
- `S` = 按键S
- `Shift` = 按键Shift
- `Space` = 按键空格
- `T` = 按键T
- `U` = 按键U
- `V` = 按键V
- `W` = 按键W
- `X` = 按键X
- `Y` = 按键Y
- `Z` = 按键Z

## LogLevel
- `Error` = 错误输出
- `Print` = 普通输出
- `Warn` = 警告输出

## MatchMode
- `All` = 全部匹配
- `Any` = 部分匹配

## MiniCurrency
- `MiniBean` = 迷你豆
- `MiniCoin` = 迷你币
- `MiniPoint` = 迷你点

## MiniMapMarkType
- `DevMark` = 使用接口创建的图标
- `Player` = 玩家图标

## MiniShopData
- `AllMountLevel` = 所有解锁等级的坐骑
- `Avt` = 所有AVT
- `Mount` = 所有坐骑
- `Skin` = 皮肤

## MiniShopPage
- `Convert` = 兑换
- `CustomCoin` = 打开自定义货币界面
- `Item` = 道具购买
- `MiniVip` = 大会员
- `Skin` = 皮肤
- `WareHouse` = 打开仓库
- `Welfare` = 福利

## MobType
- `Fly` = 飞行生物
- `Hostile` = 怪物
- `Passive` = 动物
- `Rare` = 稀有动物
- `Trixenie` = 三栖生物
- `Water` = 水生物

## MoveType
- `Auto` = 自动调整
- `Flying` = 飞行,
- `Swimming` = 游泳,
- `Walking` = 行走,

## ObjType
- `Area` = 区域
- `Block` = 方块
- `DropItem` = 掉落物
- `Entity` = 实体
- `Mob` = 生物
- `Player` = 玩家
- `Pos` = 位置
- `Projectile` = 投掷物对象
- `UI` = UI编辑界面
- `World` = 世界

## PickupActionType
- `Drop` = 放下
- `Pickup` = 拾取
- `Throw` = 投掷
- `Unbind` = 解绑

## PixelUnits
- `Percentage` = 百分比
- `Value` = 绝对值

## PlayerBodyUIHight
- `EffEct` = 头部动效
- `HpBar` = 血条
- `Nick` = 昵称
- `Title` = 称号

## PlayerMotion
- `FallGround` = 落地
- `Jump` = 跳跃
- `JumpTwice` = 二段跳
- `Run` = 奔跑
- `Sneak` = 潜行
- `Static` = 静止
- `Swim` = 游泳
- `Walk` = 行走

## PlayerNameType
- `EffEct` = 头部特效
- `Nick` = 昵称
- `Title` = 称号

## ProgressImg
- `Background` = 进度背景
- `Progress` = 进度值

## ProgressVal
- `CurAndMax` = 当前值和最大值
- `Current` = 当前值
- `Max` = 最大值
- `Min` = 最小值

## RayDetectType
- `Actor` = 生物
- `ActorType` = 生物类型
- `Block` = 方块类型
- `LiquidBlock` = 液体方块类型
- `Player` = 玩家

## RelativeCampType
- `Any` = 任意
- `Enemy` = 敌方
- `Friendly` = 友方
- `Neutral` = 中立

## RoleAttr
- `Atk` = 攻击力
- `AttackDis` = 攻击距离
- `CurHp` = 当前生命值
- `CurHunger` = 饥饿度
- `CurOxygen` = 当前氧气值
- `CurStrength` = 当前体力值
- `FlySpeed` = 飞行速度
- `Gravity` = 重力值
- `HpRecover` = 生命恢复
- `JumpPower` = 跳跃力
- `LevelExp` = 星星经验
- `MaxHp` = 最大生命值
- `MaxHunger` = 饥饿度
- `MaxOxygen` = 最大氧气值
- `MaxStrength` = 当前最大体力值
- `PunchArmor` = 近战防御
- `RangeArmor` = 远程防御
- `RunSpeed` = 奔跑速度
- `StarNum` = 星星数量
- `SwinSpeed` = 游泳速度
- `ViewDis` = 视野距离
- `WalkSpeed` = 移动速度

## RoleMotion
- `FallGround` = 落地
- `Jump` = 跳跃
- `Run` = 奔跑
- `Sneak` = 潜行
- `Stand` = 站立
- `Swim` = 游泳
- `Walk` = 行走

## RolePickupType
- `Carried` = 被举起者
- `Carrying` = 举起者

## SkyboxAttr
- `AmbientLightIntensity` = 环境光强度
- `CloudDensity` = 云的密度
- `CloudHigh` = 云的高度
- `CloudSpeed` = 云的运动速度
- `DirectionalLightIntensity` = 太阳光强度
- `FogreMaxDis` = 雾的最远距离
- `FogreMinDis` = 雾的最近距离
- `MoonScale` = 月亮大小
- `StarDensity` = 星星密度
- `SunScale` = 太阳大小
- `Template` = 模板
- `WaterMirrorness` = 水镜面度
- `WaterTransparency` = 水透明度
- `WindStrength` = 风速

## SkyboxAttrNoTime
- `Metallic` = 整体金属度
- `Roughness` = 整体粗糙度

## SkyboxColor
- `AmbientLight` = 环境光颜色
- `Bottom` = 天空底部颜色
- `Cloud` = 云颜色
- `DirectionalLight` = 太阳光颜色
- `Env` = 环境光颜色
- `Fog` = 雾颜色
- `Light` = 天空光照颜色
- `Middle` = 天空腰部颜色
- `Moon` = 月亮颜色
- `Sun` = 太阳颜色
- `Top` = 天空顶部颜色
- `Water` = 水颜色

## SkyboxFilter
- `Bloomthreshold` = Bloom阀值
- `Color` = 滤镜颜色
- `Contrast` = 对比度
- `Dof` = 景深强度-暂时没用到
- `Exposure` = 曝光强度
- `Flood` = 泛光强度（Bloom强度）
- `Gamma` = 伽马强度
- `Lut` = 色彩校正
- `Saturation` = 饱和度
- `Template` = 滤镜模板
- `Volumelight` = 体积光强度

## SkyboxMap
- `Moon` = 月亮贴图
- `Sky` = 天空贴图
- `Sun` = 太阳贴图

## SkyboxParticle
- `Randomness` = 运动不规则度
- `Range` = 范围
- `Speed` = 速度
- `Strength` = 强度

## SkyboxSwitch
- `Fogenable` = 雾开关

## SkyboxTime
- `Current` = 当前时间
- `Time0` = 天空盒0点
- `Time12` = 天空盒12点
- `Time16` = 天空盒16点
- `Time18` = 天空盒18点
- `Time20` = 天空盒20点
- `Time4` = 天空盒4点
- `Time6` = 天空盒6点
- `Time8` = 天空盒8点
- `TimeAll` = 所有时间段

## SortType
- `Down` = 降序,
- `Up` = 升序,

## TeamAttr
- `PlayerNum` = 玩家数量
- `Score` = 分数

## TeamResults
- `Dogfall` = 平局
- `Lose` = 失败
- `None` = 胜负未定
- `Win` = 胜利

## TerrainType
- `Flat` = 平坦地形
- `Normal` = 随机地形

## TurnFaceDir
- `Pitch` = 垂直朝向
- `Yaw` = 水平朝向

## UIAttr
- `Name` = 名称
- `Visibility` = 显示/隐藏状态

## UIScollDir
- `Both` = 自由滑动
- `Horizontal` = 水平滑动
- `Vertical` = 垂直滑动

## VDistanceRange
- `Far` = 远
- `Farthest` = 最远
- `Further` = 更远
- `Middle` = 中
- `Near` = 近

## VarType
- `AreaGroup` = 区域组
- `Areains` = 区域
- `BlockType` = 方块类型
- `BlockTypeGroup` = 方块类型组
- `Blueprint` = 蓝图
- `Boolean` = 布尔值
- `BooleanGroup` = 布尔值组
- `BuffType` = buff类型
- `BuffTypeGroup` = buff类型组
- `Creature` = 生物
- `CreatureGroup` = 生物组
- `CreatureType` = 生物类型
- `CreatureTypeGroup` = 生物类型组
- `DropItem` = 掉落物
- `DropItemGroup` = 掉落物组
- `EffectType` = 特效类型
- `EffectTypeGroup` = 特效类型组
- `Element` = 元件
- `ElementGroup` = 元件组
- `Entity` = 实体
- `EntityGroup` = 实体组
- `EntityType` = 实体类型
- `EntityTypeGroup` = 实体类型组
- `ItemType` = 道具类型
- `ItemTypeGroup` = 道具类型组
- `ListData` = 无需列表
- `Map` = kv map表
- `Model` = 模型
- `ModelGroup` = 模型组
- `Number` = 数值
- `NumberGroup` = 数值组
- `Object` = 对象
- `ObjectGroup` = 对象组
- `Player` = 玩家
- `PlayerGroup` = 玩家组
- `Pos` = 位置
- `PosGroup` = 位置组
- `Projectile` = 投射物
- `ProjectileGroup` = 投射物组
- `Role` = 角色
- `RoleGroup` = 角色组
- `SortedData` = 有序列表
- `Sound` = 声音
- `SoundGroup` = 声音组
- `String` = 字符串
- `StringGroup` = 字符串组
- `Table` = 二维表
- `Texture` = 纹理
- `TextureGroup` = 纹理组
- `Timer` = 定时器
- `TimerGroup` = 计时器组

## VerticalOffset
- `Bottom` = 居下
- `Centered` = 居中
- `Top` = 居上

## ViedoPlayMode
- `Once` = 单次播放
- `Repeat` = 循环播放

## ViewPortType
- `Back` = 背视角
- `Back2` = 背视角2
- `Custom` = 自定义视角
- `Front` = 正视角
- `Main` = 主视角
- `Top` = 俯视角

## WeatherGroup
- `AirIsland` = 空岛组
- `Coldzone` = 高峰寒带组
- `Common` = 常见组
- `Desert` = 沙漠组
- `Frigidzone` = 普通寒带组
- `Global` = 全局对象
- `Nunja` = 湿地组
- `Ocean` = 海洋组
- `Plain` = 平坦组
- `Volcano` = 火山组

## WeatherType
- `Custom` = 自定义
- `None` = 无天气
- `Rain` = 雨天
- `Sandstorm` = 沙尘暴
- `Snow` = 雪天
- `Sunshine` = 晴天
- `UnderWater` = 暴雨
- `Volcano` = 火山

## WorkeStage
- `Craft` = 工具箱
- `Enchant` = 附魔台
- `Repair` = 修理台

## WorldType
- `Create` = 多人创造模式
- `CreateToRungame` = 由创造模式转的生存
- `Extremity` = 极限模式
- `Freemode` = 冒险模式之自由模式
- `Gamemaker` = 自制玩法的编辑模式
- `GamemakerRun` = 自制玩法的运行模式
- `Record` = 录像模式
- `Single` = 单人模式

## lua_type
- `boolean` = 布尔值,包含两个值：false和true
- `function` = 由 C 或 Lua 编写的函数
- `nil` = 表示一个无效值(在条件表达式中相当于false)
- `number` = 实数,表示双精度类型的实浮点数,也可以是整数
- `string` = 字符串,由一对单引号或双引号来表示
- `table` = Lua的一种数据结构，可用来创建不同的数据类型，如：数组、字典等
