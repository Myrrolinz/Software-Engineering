import { shallowMount } from '@vue/test-utils';
import Register from './Register';





describe('<Register/>', () => {
	const wrapper = shallowMount(Register);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(Register);
		expect(wrapper2.html()).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

  /*
  it("slide correctly", () => {
		// 滑动 slide
		wrapper.find('slide-verification').trigger('check-result');
	  });
  		// 可以立即获取 msg 最新的值，不再需要 wrapper.vm.$nextTick();
		expect(wrapper.find('h1').text())
		  .toEqual('new message');
		  */
