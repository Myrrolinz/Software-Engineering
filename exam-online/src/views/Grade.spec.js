import { shallowMount } from '@vue/test-utils';
import Grade from './Grade';





describe('<Grade/>', () => {
	const wrapper = shallowMount(Grade);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(Grade);
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
