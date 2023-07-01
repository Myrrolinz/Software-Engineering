<template>
	<div id="answer">
		<el-container>
			<el-aside width="300px">
				<el-card class="box-card" shadow="hover">
					<time-count-down :totalTime="getExam.total_time" @hand-in="handIn"></time-count-down>
					<el-divider content-position="center">选择题</el-divider>
					<el-row class="question-tag" type="flex" justify=" space-around ">
						<el-col :span="24">
							<el-tag v-for="(item, index) in choices" :key="item.id" :type="index + 1 == current ? 'success' : ''" :effect="index + 1 == current || answer[0][index] != null ? 'dark' : 'plain'"
							 @click="changeQuestion(index + 1)">
								{{ index + 1 }}
							</el-tag>
						</el-col>
					</el-row>
					<el-divider content-position="center">填空题</el-divider>
					<el-row class="question-tag">
						<el-col :span="24">
							<el-tag v-for="(item, index) in fills" :key="item.id" :type="index + fillPos == current ? 'success' : ''"
							 :effect="index + fillPos == current || answer[1][index] != null ? 'dark' : 'plain'" @click="changeQuestion(index+fillPos)">
								{{ index + fillPos }}
							</el-tag>
						</el-col>
					</el-row>
					<el-divider content-position="center">判断题</el-divider>
					<el-row class="question-tag">
						<el-col :span="24">
							<el-tag v-for="(item, index) in judges" :key="item.id" :type="index + judgePos == current ? 'success' : ''"
							 :effect="index + judgePos == current || answer[2][index] != null ? 'dark' : 'plain'" @click="changeQuestion(index+judgePos)">
								{{ index + judgePos }}
							</el-tag>
						</el-col>

					</el-row>
					<el-divider content-position="center">作文题</el-divider>
					<el-row class="question-tag">
						<el-col :span="24">
							<el-tag v-for="(item, index) in subjective" :key="item.id" :type="index + subjectivePos == current ? 'success' : ''"
							 :effect="index + subjectivePos == current || answer[3][index] != null ? 'dark' : 'plain'" @click="changeQuestion(index+subjectivePos)">
								{{ index + subjectivePos }}
							</el-tag>
						</el-col>
					</el-row>
					<el-divider></el-divider>
					<div class="bottom clearfix">
						<el-tag type="primary" effect="dark"></el-tag>已答
						<el-tag type="primary" effect="plain"></el-tag>未答
						<el-tag type="success" effect="dark"></el-tag>当前
						<br />
						<br />
						<el-button type="primary" class="button" @click="handIn">交卷</el-button>
					</div>
				</el-card>
			</el-aside>
			<el-container>
				<el-header>
					<el-card class="box-card" shadow="hover" style="width: auto;">
						<div id="information">
							<el-row type="flex" justify="center">
								<el-col :span="4">
									<span>学号：{{getUser.username}}</span>
								</el-col>
								<el-col :span="4">
									<span>姓名：{{getStudent.name}}</span>
								</el-col>
								<el-col :span="4">
									<span>性别：{{getStudent.gender = 'M' ? '男' : '女'}}</span>
								</el-col>
								<el-col :span="4">
									<span>专业：{{clazz.major}}</span>
								</el-col>
								<el-col :span="4">
									<span>年级：{{clazz.year}}</span>
								</el-col>
								<el-col :span="4">
									<span>班级：{{clazz.clazz}}</span>
								</el-col>
							</el-row>
						</div>
					</el-card>
				</el-header>
				<el-main>
					<el-card class="box-card" shadow="hover" style="width: 1110px; height:570px;margin-top: 20px;">
						<div id="choice" v-for="(item,index) in choices" v-show="index + 1 == current">
							<h1>{{index + 1}}. {{item.question}} [{{item.score}}分]</h1>
							<el-radio-group v-model="answer[0][index]">
								<el-radio label="A" border>A. {{item.answer_A}}</el-radio><br />
								<el-radio label="B" border>B. {{item.answer_B}}</el-radio><br />
								<el-radio label="C" border>C. {{item.answer_C}}</el-radio><br />
								<el-radio label="D" border>D. {{item.answer_D}}</el-radio><br />
							</el-radio-group>
						</div>
						<div id="fill" v-for="(item, index) in fills" v-show="index + fillPos == current">
							<h1>{{index + fillPos}}. {{item.question}} [{{item.score}}分]</h1>
							<el-input v-model="answer[1][index]"></el-input>
						</div>
						<div id="judge" v-for="(item, index) in judges" v-show="index + judgePos == current">
							<h1>{{index + judgePos}}. {{item.question}} [{{item.socre}}分]</h1>
							<el-radio-group v-model="answer[2][index]">
								<el-radio label="T" border>正确</el-radio><br />
								<el-radio label="F" border>错误</el-radio><br />
							</el-radio-group>
						</div>
						<div id="subjective" v-for="(item, index) in subjective" v-show="index + subjectivePos == current">
							<h1>{{index + subjectivePos}}. {{item.question}} [{{item.score}}分]</h1>
							<el-row type="flex" justify="space-around">
								<el-col :span="10">
									主观题书写区域
									<el-input type="textarea" :autosize="{ minRows: 18, maxRows: 18}" v-model="answer[3][index]">
									</el-input>
								</el-col>
							</el-row>
						</div>
					</el-card>
				</el-main>
				<el-footer>
					<div class="box-div">
						<el-row type="flex" justify="start">
							<el-col :span="4" :offset="6">
								<el-button type="primary" @click="lastQuestion">上一题</el-button>
							</el-col>
							<el-col :span="4">
								<el-button type="primary" @click="nextQuestion">下一题</el-button>
							</el-col>
						</el-row>
					</div>
				</el-footer>
			</el-container>
		</el-container>
	</div>
</template>

<script>
	import TimeCountDown from '@/components/TimeCountDown.vue'
  //创建8位字符串标识符，每次页面刷新的时候都会获得新的标识符
  function generateRandomString() {
      let result = '';
      let characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
      let charactersLength = characters.length;
      for (let i = 0; i < 8; i++) {
          result += characters.charAt(Math.floor(Math.random() * charactersLength));
      }
      return result;
  }
  var identifier = generateRandomString();

	export default {
		data() {
			return {
				clazz: {},
				choices: [],
				fills: [],
				judges: [],
				subjective: [],
				answer: [
					[],
					[],
					[],
					[]
				], //保存已作答的答案
				current: 1, //当前题号
				totalScore: 0, //总分
				testMsg: "", //编程题测试信息
			}
		},
		components: {
			TimeCountDown
		},
		computed: {
			//用计算属性显示结果
			fillPos() {
				return this.choices.length + 1;
			},
			judgePos() {
				return this.choices.length + this.fills.length + 1;
			},
			subjectivePos() {
				return this.choices.length + this.fills.length + this.judges.length + 1;
			},
			totalNum() {
				return this.choices.length + this.fills.length + this.judges.length + this.subjective.length;
			},
			getStudent() {
				return this.$store.state.student;
			},
			getUser() {
				return this.$store.state.user;
			},
			getPaper() {
				return localStorage.getItem('paper') ? JSON.parse(localStorage.getItem('paper')) : {};
			},
			getExam() {
				return localStorage.getItem('exam') ? JSON.parse(localStorage.getItem('exam')) : {};
			},
			getPractice() {
				return localStorage.getItem('practice') ? JSON.parse(localStorage.getItem('practice')) : {};
			},
			isPractice() {
				return this.$store.state.isPractice;
			}
		},
		methods: {
			// 获取班级信息
			getClazzInfo() {
				this.$axios(`/api/clazzs/${this.getStudent.clazz}/?format=json`).then(res => {
					console.log(res.data)
					this.clazz = res.data
				}).catch(error => {
					console.log(error)
				})
			},
			// 获取选择题
			getChoiceInfo() {
				this.$axios(`/api/choices/?format=json`, {
					params: {
						choice_number: this.getPaper.choice_number,
						level: this.getPaper.level
					}
				}).then(res => {
					this.choices = res.data
					console.log(this.choices)
				}).catch(error => {
					console.log(error)
				})
			},
			// 获取填空题
			getFillInfo() {
				this.$axios('/api/fills/?format=json', {
					params: {
						fill_number: this.getPaper.fill_number,
						level: this.getPaper.level
					}
				}).then(res => {
					this.fills = res.data
					console.log(this.fills)
				}).catch(error => {
					console.log(error)
				})
			},
			// 获取判断题
			getJudgeInfo() {
				this.$axios(`/api/judges/?format=json`, {
					params: {
						judge_number: this.getPaper.judge_number,
						level: this.getPaper.level
					}
				}).then(res => {
					this.judges = res.data
					console.log(this.judges)
				}).catch(error => {
					console.log(error)
				})
			},
			// 获取主观题
			getProgramInfo() {
				this.$axios(`/api/subjective/?format=json`, {
					params: {
						subjective_number: this.getPaper.subjective_number,
						level: this.getPaper.level
					}
				}).then(res => {
					this.subjective = res.data
					console.log(this.subjective)
					//如果是编程题，第一次加载答题模板
					this.loadProgram();
				}).catch(error => {
					console.log(error)
				})
			},
			// 下一题
			nextQuestion() {
				console.log(this.current,this.totalNum)
				if (this.current == this.totalNum) {
					this.$message("已经是最后一题了！")
				} else {
					this.current += 1
				}
				//如果是编程题，第一次加载答题模板
				this.loadProgram();
			},
			// 上一题
			lastQuestion() {
				if (this.current == 1) {
					this.$message("已经是第一题了！")
				} else {
					this.current -= 1
				}
				//如果是编程题，第一次加载答题模板
				this.loadProgram();
			},
			// 点击切换题目
			changeQuestion(number) {
				this.current = number
				//如果是编程题，第一次加载答题模板
				this.loadProgram();
			},
			// 第一次加载编程题答题模板
			loadProgram() {
				let index = this.current - parseInt(this.subjectivePos)
				if (index >= 0 && this.answer[3][index] == null) {
					this.answer[3][index] = this.subjective[index].answer_template;
				}
				// 清空输出信息
				this.testMsg = null;
			},
			//阅卷
			goOverPaper() {
				this.totalScore = 0;
				this.goOverChoice();
				this.goOverFill();
				this.goOverJudge();
				this.goOverProgram();
			},
			//选择题阅卷
			goOverChoice() {
				for (let i = 0; i < this.choices.length; i++) {
					if (this.isPractice == true) {
						axios.post(`api/records/choices/`, {
							practice_id: this.getPractice.id,
							student_id: this.getStudent.id,
							choice_id: this.choices[i].id,
							your_answer: this.answer[0][i]
						}).then(res => {
							console.log(res); //处理成功的函数 相当于success

						}).catch(function(error) {
							console.log(error) //错误处理 相当于error
						});
					}
					//判断是否正确
					if (this.choices[i].right_answer == this.answer[0][i]) {
						this.totalScore += this.choices[i].score;
					}
				}
			},
			//填空题阅卷
			goOverFill() {
				for (let i = 0; i < this.fills.length; i++) {
					//如果是模拟练习，保存答题记录
					if (this.isPractice == true) {
						axios.post(`api/records/fills/`, {
							practice_id: this.getPractice.id,
							student_id: this.getStudent.id,
							fill_id: this.fills[i].id,
							your_answer: this.answer[1][i]
						}).then(res => {
							console.log(res); //处理成功的函数 相当于success

						}).catch(function(error) {
							console.log(error) //错误处理 相当于error
						});
					}
					//判断是否正确
					if (this.fills[i].right_answer == this.answer[1][i]) {
						this.totalScore += this.fills[i].score;
					}
				}
			},
			//判断题阅卷
			goOverJudge() {
				for (let i = 0; i < this.judges.length; i++) {
					//如果是模拟练习，保存答题记录
					if (this.isPractice == true) {
						axios.post(`api/records/judges/`, {
							practice_id: this.getPractice.id,
							student_id: this.getStudent.id,
							judge_id: this.judges[i].id,
							your_answer: this.answer[2][i]
						}).then(res => {
							console.log(res); //处理成功的函数 相当于success

						}).catch(function(error) {
							console.log(error) //错误处理 相当于error
						});
					}
					//判断是否正确
					if (this.judges[i].right_answer == this.answer[2][i]) {
						this.totalScore += this.judges[i].score;
					}
				}
			},
			//主观题阅卷
			goOverProgram: async function() {
				for (let i = 0; i < this.subjective.length; i++) {
					//判断是否正确
					await axios.post(`api/upload-subjective/`, {
						'answer': this.answer[3][i] == undefined ? '' : this.answer[3][i],
            "exam_id": this.getExam.id,
						"student_id": this.getStudent.id,
            "question_id":this.subjective[i].id,
            "identifier": identifier,
					}).then(res => { //处理成功的函数 相当于success
						if (res && res.data.message == "success") {
							console.log("上传成功！")
						}
						//如果是模拟练习，保存答题记录
						if (this.isPractice == true) {
							axios.post(`api/records/programs/`, {
								practice_id: this.getPractice.id,
								student_id: this.getStudent.id,
								subjective_id: this.subjective[i].id,
								your_answer: this.answer[3][i],
								cmd_msg: res.data.message
							}).then(res => {
								console.log(res); //处理成功的函数 相当于success

							}).catch(function(error) {
								console.log(error) //错误处理 相当于error
							});
						}
					}).catch(function(error) {
						//错误处理 相当于error
					})
				}
			},
			//交卷
			handIn() {
				this.goOverPaper();
				const temp = this
				clearTimeout(this.timer); //清除延迟执行
				this.timer = setTimeout(() => { //设置延迟执行
					if (this.isPractice == true) {
						this.$message({
							message: '你本次的测试客观题成绩为：' + this.totalScore + '分',
							type: 'success'
						});
						//跳转到模拟练习
						this.$router.push('/practice')
					} else {
						this.$message({
							message: '你本次的考试客观题成绩为：' + this.totalScore + '分',
							type: 'success'
						});
						// 考试成绩存库
						axios.post(`api/grades/`, {
							"exam_id": this.getExam.id,
							"student_id": temp.getStudent.id,
							"score": this.totalScore,
              "identifier": identifier,
						}).then(res => { //处理成功的函数 相当于success
							//跳转到我的成绩
							this.$router.push('/grade')
						}).catch(function(error) {
							//错误处理 相当于error
						})

					}
				}, 1000);
			}
		},
		created() {
			this.getClazzInfo();
			this.getChoiceInfo();
			this.getFillInfo();
			this.getJudgeInfo();
			this.getProgramInfo();
		},
	}
</script>

<style lang="scss" scoped>
	.el-header {}

	.el-aside {
		margin-left: 50px;
	}

	.el-main {}

	.el-footer {}

	.el-footer .el-row {
		margin-top: 10px;
	}

	#information {
		margin-top: 20px;
	}

	.box-div {
		border-radius: 2px;
	}

	.box-card {
		width: 250px;
		border-radius: 2px;
	}

	.question-tag {
		text-align: left;
	}

	.el-tag {
		margin-top: 5px;
		margin-left: 10px;
		width: 30px;
		height: 30px;
	}

	.bottom .el-tag {
		width: 20px;
		height: 20px;
	}

	#choice {
		float: left;
		width: auto;
		text-align: left;
	}

	#choice .el-radio-group {
		margin-left: 20px;
		text-align: left;
	}

	#choice .el-radio {
		margin-top: 40px;
	}

	#fill {
		float: left;
		width: auto;
		text-align: left;
	}

	#fill .el-input {
		margin-top: 20px;
		margin-left: 30px;
	}

	#judge {
		float: left;
		width: auto;
		text-align: left;
	}

	#judge .el-radio {
		margin-top: 40px;
	}

	#subjective {
		float: left;
		width: 1000px;
	}
</style>
